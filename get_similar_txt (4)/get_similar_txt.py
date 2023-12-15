import spacy
import json
nlp = spacy.load('en_core_web_md')


def get_similarity(url_domain,query):

    # url_domain = "incometaxindia"

    file_data = open(f"./webData/{url_domain}.json",encoding='utf-8')

    data = json.load(file_data)
    # doc2_query = "who can benefit from new tax regime?"

    doc2 = nlp(query)
    final_para = []
    for key,val in data.items():

        # doc1_para = r"""Minimum Alternate Tax (MAT)\nA foreign company is liable to pay Minimum Alternate Tax where tax payable by it, on total income computed as per normal provisions of the Act, is less than 15% of 'book profit'.In such a case the 'book profit' is taken as the income of the company and it shall be liable to pay tax at the rate of 15% of such 'book profit'.However, the provisions of MAT do not apply in case of foreign companies if it does not have permanent establishment (PE) in India or opts for presumptive taxation scheme of Section 44B, Section 44BB, Section 44BBA or Section 44BBB.6.Co-operative Society\nAssessment Years 2023-24 and 2024-25 Taxable income\nTax Rate Up to Rs.10,000\n10% Rs.10,000 to Rs.20,000\n20% Above Rs.20,000\n30% Add: (a) (a) Surcharge: The amount of income-tax shall be increased by a surcharge at the rate of 7% of such tax, where total income exceeds one crore rupees but not exceeding ten crore rupees and at the rate of 12% of such tax, where total income exceeds ten crore rupees.However, the surcharge shall be subject to marginal relief, which shall be as under:\n(i) Where income exceeds one crore rupees but not exceeding ten crore rupees, the total amount payable as income-tax and surcharge shall not exceed total amount payable as income-tax on total income of one crore rupees by more than the amount of income that exceeds one crore rupees.(ii) Where income exceeds ten crore rupees, the total amount payable as income-tax and surcharge shall not exceed total amount payable as income-tax on total income of ten crore rupees by more than the amount of income that exceeds ten crore rupees.(b) Health and Education Cess: The amount of income-tax and the applicable surcharge, shall be further increased by health and education cess calculated at the rate of four percent of such income-tax and surcharge.Note: (a)\tA co-op.society is liable to pay Alternate Minimum Tax where tax payable by it, on total income computed as per normal provisions of the Act, is less than 15% of 'adjusted total income'.In such a case the 'adjusted total income' is taken as the income of co-op"""
        doc1 = nlp(val)

        # print(type(doc1.similarity(doc2)))
        # print(doc1.similarity(doc2))
        if doc1.similarity(doc2) > 0.4:
            final_para.append(val)

    # print("final_para-----",final_para)

    return "".join(final_para)






 