import openpyxl
import json
import random


alias_keywords=['{}有其他别名嘛','{}别名是什么','{}还有其他称呼','{}别称','{}别名','{}还可以怎么叫','{}其他名字','{}哪些别称']
smell_keywords=['{}什么气味','{}什么味道','{}闻起来怎么样','{}什么味的','{}吃起来苦嘛','{}吃了是什么味','{}有毒嘛','{}有毒性嘛']
cure_keywords=['{}可以治什么','{}治哪些病','{}可以治什么症状','{}有那些食用方法','{}如何食用','{}最佳食用方法','{}有什么好处', '{}有什么益处', '{}有何益处','{}用来做啥', '{}用来作甚','{}治愈啥', '{}主治啥', '{}主治什么', '{}有什么用', '{}有何用']
part_keywords=['{}属于什么部类','{}属于什么部','{}什么部类', '{}什么部', '{}哪个部类', '{}哪个部']

def process_excel_to_json(input_files, output_file):
    for input_file in input_files:
        # Load the workbook
        wb = openpyxl.load_workbook(input_file)

        # Select the "DrugQA" sheet
        sheet = wb["Sheet1"]

        # Initialize the output data structure
        output_data = []

        # Iterate through each row in column A and D
        for row in sheet.iter_rows(min_row=2, max_col=5, values_only=True):
            system_value = "您是一位非常专业的的中医药学教授。您始终根据提问者的问题提供准确、全面和详细的答案。"

            # Create the conversation dictionary
            print(row[1],len(row))
            if len(row[0])>0:
                for i in random.sample([k for k in range(len(part_keywords))], random.randint(int(len(part_keywords)/2),len(part_keywords))):
                    conversation = {
                        "system": system_value,
                        "input": part_keywords[i].format(row[1]),
                        #"output": {"name":row[1],"question_type":"part","answer":row[0]}
                        "output": json.dumps({"name":row[1],"question_type":"part","answer":row[0]},ensure_ascii=False)
                    }

                    # Append the conversation to the output data
                    output_data.append({"conversation": [conversation]})

            if len(row)>=3:
                if row[2]:
                    for i in random.sample([k for k in range(len(alias_keywords))], random.randint(int(len(alias_keywords)/2),len(alias_keywords))):
                        conversation = {
                            "system": system_value,
                            "input": alias_keywords[i].format(row[1]),
                            #"output": {"name":row[1],"question_type":"alias","answer":row[2]}
                            "output": json.dumps({"name":row[1],"question_type":"alias","answer":row[2]},ensure_ascii=False)
                        }

                        # Append the conversation to the output data
                        output_data.append({"conversation": [conversation]})

            if len(row)>=4:
                if row[3]:
                    for i in random.sample([k for k in range(len(smell_keywords))], random.randint(int(len(smell_keywords)/2),len(smell_keywords))):
                        conversation = {
                            "system": system_value,
                            "input": smell_keywords[i].format(row[1]),
                            #"output": {"name":row[1],"question_type":"smell","answer":row[3]}
                            "output": json.dumps({"name":row[1],"question_type":"smell","answer":row[3]},ensure_ascii=False)
                        }

                        # Append the conversation to the output data
                        output_data.append({"conversation": [conversation]})

            if len(row)>=5:
                if row[4]:
                    for i in random.sample([k for k in range(len(cure_keywords))], random.randint(int(len(cure_keywords)/2),len(cure_keywords))):
                        conversation = {
                            "system": system_value,
                            "input": cure_keywords[i].format(row[1]),
                            #"output": {"name":row[1],"question_type":"cure","answer":row[4]}
                            "output": json.dumps({"name":row[1],"question_type":"cure","answer":row[4]},ensure_ascii=False)
                        }

                        # Append the conversation to the output data
                        output_data.append({"conversation": [conversation]})

    # Write the output data to a JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(output_data, json_file, indent=4,ensure_ascii=False)

    print(f"Conversion complete. Output written to {output_file}")

# Replace 'MedQA2019.xlsx' and 'output.jsonl' with your actual input and output file names
process_excel_to_json(['./data/xlsx_all/ChineseMedicalData.xlsx'], './data/jsonl/output.jsonl')
