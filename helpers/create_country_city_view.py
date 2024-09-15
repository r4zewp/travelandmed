from config.models import user, country, city

def create_country_city_text(query_result: [str]) -> str:
    """
    Formats a query for country & city select into string for bot message
    :param query_result: - Should be list of Dicts
    """
    final_string = ''
    for cnt in query_result:
        n_cnt = country.Country.from_json(cnt)
        ct_string = '*Города:*\n'
        for ct in n_cnt.cities:
            new_name = str(ct.name).replace(')', '').replace('(', '').replace("'", '')
            ct_string += f' - {new_name}\n'
        ct_cnt_string = f'*Страна:* {n_cnt.name_ru}\n' + ct_string
        final_string += ct_cnt_string
        final_string += '\n'
    print(final_string)
    return final_string


