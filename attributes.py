import commons


def general_agreement_number(policy_list):
    return commons.find_in_list(policy_list, ['generalAgreementNumber'])


def message_list(policy_list):
    mess_list = commons.find_in_list(policy_list, ['messageList'])

    return mess_list[0] if len(mess_list) > 0 else ''


def premium(policy_list):
    return commons.find_in_list(policy_list, ['premium', 'value'])


def run_rule(policy_list):
    run_rule_list = []

    for policy in policy_list:
        run_rule_list = [attributes['value'] for attributes in policy['attributeList'] if attributes['symbol'] == 'PPRunRuleId']

    return run_rule_list if len(run_rule_list) > 0 else ''


def product(policy_list):
    return commons.find_in_list(policy_list, ['productData', 'symbol'])


def postal_code(policy_list):
    postal_code_list = []

    try:
        for policy in policy_list:
            for obj in policy['objectList']:
                attribute = commons.find_attribute(obj, ['estate', 'address', 'postalCode'])
                if attribute:
                    postal_code_list.append(attribute)

    except Exception as e:
        postal_code_list = []

    return postal_code_list if len(postal_code_list) > 0 else ''


def property_type(policy_list):
    property_list = []

    try:
        for policy in policy_list:
            for obj in policy['objectList']:
                attribute = commons.find_attribute(obj, ['estate', 'name'])
                if attribute:
                    property_list.append(attribute)

    except Exception as e:
        property_list = []

    return property_list if len(property_list) > 0 else ''


def property_price(postal_code, property_type, attribute):
    baza = commons.get_data_from_pickle(r'files/baza.pickle')
    dictionary = dict(zip(property_type, postal_code))

    price = [baza[f'baza_mieszkan_{attribute}'][value] if key == 'MIESZKANIE' else baza[f'baza_domow_{attribute}'][value] if key == 'DOM' else None for key, value in dictionary.items()]

    # for key, value in dictionary.items():
    #     if key == 'MIESZKANIE':
    #         price.append(baza[f'baza_mieszkan_{attribute}'][value])
    #     if key == 'DOM':
    #         price.append(baza[f'baza_domow_{attribute}'][value])

    return price if len(price) > 0 else ''


def attribute_from_attribute_list(policy_list, attribute):
    for policy in policy_list:
        attribute_list = [attr['value'] for attr in policy['attributeList'] if attr['symbol'] == attribute]

    return attribute_list if len(attribute_list) > 0 else ''


def operation_type(operation_list):
    return commons.find_in_list(operation_list, ['operationType'])


def policy_is_payed_oc(earnix):
    return [att['PolicyIsPayedOC'] for att in earnix['data'] if len(str(commons.find_deep_field(att, ['PolicyIsPayedOC'], None))) > 0]


def ufg_car_insur_end_date_last_policy_oc(earnix):
    for att in earnix['data']:
        if commons.find_deep_field(att, ['UFGCarInsurEndDateLastPolicyOC'], None) and len(str(commons.find_deep_field(att, ['UFGCarInsurEndDateLastPolicyOC'], None))) > 0:
            return att['UFGCarInsurEndDateLastPolicyOC']
        else:
            return []


def ufg_car_insur_end_date_last_policy_ac(earnix):
    for att in earnix['data']:
        if commons.find_deep_field(att, ['UFGCarInsurEndDateLastPolicyAC'], None) and len(str(commons.find_deep_field(att, ['UFGCarInsurEndDateLastPolicyAC'], None))) > 0:
            return att['UFGCarInsurEndDateLastPolicyAC']
        else:
            return []


def active_oc(policy):
    return [attribute_from_attribute_list(pol['riskList'], 'ActiveOC') for pol in policy if attribute_from_attribute_list(pol['riskList'], 'ActiveOC')]


def risks_J07_J08(policy):
    all_risk = []

    for pol in policy:
        risks = [risk['productData']['symbol'] for risk in pol['riskList'] if risk['productData']['symbol'] == 'J08' or risk['productData']['symbol'] == 'J07']
        if 'J07' in risks and 'J08' in risks:
            all_risk.append(['J07', 'J08'])
        elif 'J07' in risks:
            all_risk.append(['J07'])
        else:
            all_risk.append(['J08'])
    return all_risk


def all_risks(policy):
    return [risk['productData']['symbol'] for pol in policy for risk in pol['riskList']]


def calculation_algorithm(policy):
    alg_list = []

    for pol in policy:
        for risk in pol['riskList']:
            try:
                alg_list.append(risk['calculationAlgorithm'])
            except:
                pass

    return alg_list
