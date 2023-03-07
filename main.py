import glob
import os.path
import pandas as pd
import attributes
import commons

response_one_path = glob.glob('files/response_one/*', recursive=True)
earnix_one_path = glob.glob('files/earnix_one/*', recursive=True)

response_two_path = glob.glob('files/response_two/*', recursive=True)
earnix_two_path = glob.glob('files/earnix_two/*', recursive=True)

excel_path = r'files/statystyka.xlsx'

list_all = []
list_to_df = {}
a = {}
b = 0
for tariff_one in response_one_path:
    for tariff_two in response_two_path:
        if os.path.basename(tariff_one) == os.path.basename(tariff_two):
            tariff_1 = commons.load_json_file(tariff_one)
            tariff_2 = commons.load_json_file(tariff_two)

            policy_one = tariff_1['root']['applicationList'][0]['policyList']
            policy_two = tariff_2['root']['applicationList'][0]['policyList']

            sales_transaction_id_one = attributes.attribute_from_attribute_list(policy_one, 'SalesTransactionID')
            sales_transaction_id_two = attributes.attribute_from_attribute_list(policy_two, 'SalesTransactionID')

            request_id_one = attributes.attribute_from_attribute_list(policy_one, 'RequestID')
            request_id_two = attributes.attribute_from_attribute_list(policy_two, 'RequestID')

            # operation_type_one = attributes.operation_type(tariff_1['root']['applicationList'][0]['operationList'])
            # operation_type_two = attributes.operation_type(tariff_2['root']['applicationList'][0]['operationList'])

            general_agreement_number_one = attributes.general_agreement_number(policy_one)
            general_agreement_number_two = attributes.general_agreement_number(policy_two)

            message_list_one = attributes.message_list(policy_one)
            message_list_two = attributes.message_list(policy_two)

            premium_one = attributes.premium(policy_one)
            premium_two = attributes.premium(policy_two)

            run_rule_one = attributes.run_rule(policy_one)
            run_rule_two = attributes.run_rule(policy_two)

            postal_code_one = attributes.postal_code(policy_one)
            postal_code_two = attributes.postal_code(policy_two)

            property_type_one = attributes.property_type(policy_one)
            property_type_two = attributes.property_type(policy_two)

            property_price_one = attributes.property_price(postal_code_one, property_type_one, 'old')
            property_price_two = attributes.property_price(postal_code_two, property_type_two, 'new')

            calculation_algorithm_one = attributes.calculation_algorithm(policy_one)
            calculation_algorithm_two = attributes.calculation_algorithm(policy_two)

            all_risks_one = attributes.all_risks(policy_one)
            all_risks_two = attributes.all_risks(policy_two)

            # znalezienie ryzyk J07 i J08
            # risks_J07_J08_one = attributes.risks_J07_J08(policy_one)
            # risks_J07_J08_two = attributes.risks_J07_J08(policy_two)

            # znalezienie atrybutu ActiveOC
            # active_oc_one = attributes.active_oc(policy_one)
            # active_oc_two = attributes.active_oc(policy_two)

            # zczytywanie atrybutów z earnix'a
            # policy_is_payed_oc_one = []
            # policy_is_payed_oc_two = []
            # for earnix_one in earnix_one_path:
            #
            #     if os.path.basename(earnix_one) == os.path.basename(tariff_one):
            #         earnix_1 = commons.load_json_file(earnix_one)
            #
            #         policy_is_payed_oc_one = attributes.policy_is_payed_oc(earnix_1)
            #
            # for earnix_two in earnix_two_path:
            #
            #     if os.path.basename(earnix_two) == os.path.basename(tariff_one):
            #         earnix_2 = commons.load_json_file(earnix_two)
            #
            #         policy_is_payed_oc_two = attributes.policy_is_payed_oc(earnix_2)

            # UFGCarInsurEndDateLastPolicyOC i UFGCarInsurEndDateLastPolicyAC
            ufg_car_insur_end_date_last_policy_oc_one = None
            ufg_car_insur_end_date_last_policy_oc_two = None
            ufg_car_insur_end_date_last_policy_ac_one = None
            ufg_car_insur_end_date_last_policy_ac_two = None

            for earnix_one in earnix_one_path:

                if os.path.basename(earnix_one) == os.path.basename(tariff_one):
                    earnix_1 = commons.load_json_file(earnix_one)

                    ufg_car_insur_end_date_last_policy_oc_one = attributes.ufg_car_insur_end_date_last_policy_oc(earnix_1)
                    ufg_car_insur_end_date_last_policy_ac_one = attributes.ufg_car_insur_end_date_last_policy_ac(earnix_1)

            for earnix_two in earnix_two_path:

                if os.path.basename(earnix_two) == os.path.basename(tariff_one):
                    earnix_2 = commons.load_json_file(earnix_two)

                    ufg_car_insur_end_date_last_policy_oc_two = attributes.ufg_car_insur_end_date_last_policy_oc(earnix_2)
                    ufg_car_insur_end_date_last_policy_ac_two = attributes.ufg_car_insur_end_date_last_policy_ac(earnix_2)
        list_all.append({
            'response': os.path.basename(tariff_one),
            'product': attributes.product(policy_one),
            'SalesTransactionID_one': sales_transaction_id_one,
            'SalesTransactionID_two': sales_transaction_id_two,
            'SalesTransactionID': commons.compare_files(sales_transaction_id_one, sales_transaction_id_two),
            'RequestID_one': request_id_one,
            'RequestID_two': request_id_two,
            'RequestID': commons.compare_files(request_id_one, request_id_two),
            # 'operationType_one': operation_type_one,
            # 'operationType_two': operation_type_two,
            # 'generalAgreementNumber_one': general_agreement_number_one,
            # 'generalAgreementNumber_two': general_agreement_number_two,
            # 'generalAgreementNumber': commons.compare_files(general_agreement_number_one, general_agreement_number_two),
            'messageList_one': message_list_one,
            'messageList_two': message_list_two,
            'messageList': commons.compare_files(message_list_one, message_list_two),
            'premium_one': premium_one,
            'premium_two': premium_two,
            'premium': commons.compare_files(premium_one, premium_two),
            'runRule_one': run_rule_one,
            'runRule_two': run_rule_two,
            'runRule': commons.compare_files(run_rule_one, run_rule_two),
            # 'calculationAlgorithm_one': calculation_algorithm_one,
            # 'calculationAlgorithm_two': calculation_algorithm_two,
            # 'calculationAlgorithm': commons.compare_files(calculation_algorithm_one, calculation_algorithm_two),
            'all_risks_one': all_risks_one,
            'all_risks_two': all_risks_two,
            'all_risks': commons.compare_files(all_risks_one, all_risks_two),
            'UFGCarInsurEndDateLastPolicyOC_one': ufg_car_insur_end_date_last_policy_oc_one,
            'UFGCarInsurEndDateLastPolicyOC_two': ufg_car_insur_end_date_last_policy_oc_two,
            'UFGCarInsurEndDateLastPolicyOC': commons.compare_files(ufg_car_insur_end_date_last_policy_oc_one, ufg_car_insur_end_date_last_policy_oc_two),
            'UFGCarInsurEndDateLastPolicyAC_one': ufg_car_insur_end_date_last_policy_ac_one,
            'UFGCarInsurEndDateLastPolicyAC_two': ufg_car_insur_end_date_last_policy_ac_two,
            'UFGCarInsurEndDateLastPolicyAC': commons.compare_files(ufg_car_insur_end_date_last_policy_ac_one, ufg_car_insur_end_date_last_policy_ac_two),
            # 'postal_code_one': postal_code_one,
            # 'postal_code_two': postal_code_two,
            # 'postal_code': commons.compare_files(postal_code_one, postal_code_two),
            # 'property_type_one': property_type_one,
            # 'property_type_two': property_type_two,
            # 'property_type': commons.compare_files(property_type_one, property_type_two),
            # 'property_price_one': property_price_one,
            # 'property_price_two': property_price_two,
            # 'property_price': commons.compare_files(property_price_one, property_price_two),
            # 'PolicyIsPayedOC_one': policy_is_payed_oc_one,
            # 'PolicyIsPayedOC_two': policy_is_payed_oc_two,
            # 'PolicyIsPayedOC': commons.compare_files(policy_is_payed_oc_one, policy_is_payed_oc_two),
            # 'active_oc_one': active_oc_one,
            # 'active_oc_two': active_oc_two,
            # 'active_oc': commons.compare_files(active_oc_one, active_oc_two),
            # 'risks_J07_J08_one': risks_J07_J08_one,
            # 'risks_J07_J08_two': risks_J07_J08_two,
            # 'risks_J07_J08': commons.compare_files(risks_J07_J08_one, risks_J07_J08_two),
        })

# print(list_all)
df = pd.DataFrame(list_all)
df.to_excel(rf'{excel_path}', engine='openpyxl')
