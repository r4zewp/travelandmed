from loader import *

# States
from aiogram.fsm.context import FSMContext
from states.form import Form

# KBS
from kbs.start_kb import build_start_kb
from kbs.existing_user_kb import build_existing_user_kb

# Models
from config.models.user import User

# Handlers
from handlers import user_signup

@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext, supabase) -> None:

    query_result = (supabase
                .table('users')
                .select('*')
                .eq('tid', message.from_user.id)
                .execute()
                ).data

    if len(query_result) > 0:
        bot_user = User.from_json(query_result[0])

        if bot_user:
            await bot.send_message(chat_id=message.chat.id,
                                   text=build_welcome_back(uname=bot_user.username),
                                   parse_mode=ParseMode.MARKDOWN_V2,
                                   reply_markup=build_existing_user_kb())

    else:
        await state.set_state(Form.phone)
        await state.set_data(
            data=
            {
                'username': message.from_user.username if message.from_user.username else 'no_username',
                'tg_id': message.from_user.id
            }
        )
        await bot.send_message(chat_id=message.from_user.id,
                               text=phone_to_continue,
                               reply_markup=build_start_kb(),
                               parse_mode=ParseMode.HTML)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())





