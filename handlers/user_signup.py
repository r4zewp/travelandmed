from helpers.create_country_city_view import create_country_city_text
from loader import *

# Errors
from postgrest import APIError

# States
from aiogram.fsm.context import FSMContext
from states.form import Form

# KBS
from aiogram.types import ReplyKeyboardRemove
from kbs.countries_kb import build_countries_kb

# Helpers
from helpers.create_view import create_view

# Models
from config.models import user, country, city

user_selection = {}

@user_router.message(Form.phone)
async def handle_name(message: Message, state: FSMContext) -> None:
    await state.update_data(
        {
            "phone_number": message.contact.phone_number,
            "name": message.contact.first_name + ' ' + message.contact.last_name if message.contact.last_name else "-",
        },
    )
    await state.set_state(Form.name)
    await bot.send_message(chat_id=message.chat.id,
                           text=fill_name,
                           reply_markup=ReplyKeyboardRemove(),
                           )

@user_router.message(Form.name)
async def handle_pref_country(message: Message, state: FSMContext, supabase) -> None:
    await state.update_data({'name_input': message.text})
    await state.set_state(Form.preferred_country)

    await bot.send_message(chat_id=message.chat.id,
                           text=saving_data,
                           parse_mode=ParseMode.MARKDOWN_V2)

    # saving new user
    try:
        resp=(supabase
            .table('users')
            .insert(
                {
                    'tid': message.from_user.id,
                    'name': message.text,
                    'username': message.from_user.username
                }
            )
            .execute()
        )

        created_user = user.User.from_json(resp.data[0])

        await state.update_data({'user': created_user} )
        await bot.send_message(chat_id=message.chat.id,
                               text=saving_done,
                               parse_mode=ParseMode.MARKDOWN_V2)

    except APIError as exc:
        if exc.code == '23505':
            await bot.send_message(chat_id=message.chat.id,
                                   text=user_exists,
                                   parse_mode=ParseMode.MARKDOWN_V2)
            await bot.send_message(chat_id=message.chat.id,
                                   text=skipping,
                                   parse_mode=ParseMode.MARKDOWN_V2)
        else:
            logging.log(level=1, msg=str(exc))
            print(exc.message)

    countries = (
        supabase
        .table('countries')
        .select('*, cities(*)')
        .execute()
    )

    countries_list = []
    for cnt in countries.data:
        countries_list.append(country.Country.from_json(cnt))

    await bot.send_message(chat_id=message.chat.id,
                           text=pref_country + pref_country_list,
                           reply_markup=
                           build_countries_kb(
                               countries=countries_list,
                               selected_options=user_selection[f'{message.from_user.id}'] if user_selection[f'{message.from_user.id}'] else [],
                               uid=message.from_user.id)
                           )

# // TODO: Закончить обновление стейта выбранного для каждого пользователя при выборе страны
# @user_router.callback_query()


    # // TODO: не забыть где-нить заюзать
    # await bot.send_message(chat_id=message.chat.id,
    #                        text=pref_country + pref_country_list + '\n' +
    #                             create_country_city_text(query_result=countries.data),
    #                        parse_mode=ParseMode.MARKDOWN)


@user_router.message(Form.preferred_country)
async def handle_your_faculty(message:Message, state: FSMContext) -> None:
    await state.update_data({"pref_country": message.text})
    await state.set_state(Form.your_faculty)
    await bot.send_message(chat_id=message.chat.id,
                          text=faculty_choose + "\n" + faculty_example,
                           parse_mode=ParseMode.MARKDOWN_V2)

@user_router.message(Form.your_faculty)
async def handle_pref_sphere(message: Message, state: FSMContext) -> None:
    await state.update_data({'your_faculty': message.text})
    await state.set_state(Form.preferred_sphere)

@user_router.message(Form.preferred_sphere)
async def finish_form(message: Message, state: FSMContext) -> None:

    data = await state.get_data()
    await state.clear()
    await message.reply(text=create_view(
        name=data['name'],
        name_input=data['name_input'],
        username=data['username'],
        phone_number=data['phone_number'],
        pref_sphere=data['pref_sphere'],
        pref_country=data['pref_country'],
    ),
        parse_mode=ParseMode.HTML
    )