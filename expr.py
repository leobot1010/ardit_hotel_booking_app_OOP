import pandas as pd
from fpdf import FPDF


df = pd.read_csv('articles.csv', dtype=str)


class Articles:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.article_id, "price"].squeeze()

    def reduce_stock_by_one(self):
        stock_level = df.loc[df['id'] == self.article_id, 'in stock'].squeeze()
        df.loc[df["id"] == self.article_id, "in stock"] = int(stock_level) - 1
        df.to_csv("articles.csv", index=False)
        return stock_level


class Pdf:
    def __init__(self, article_object):
        self.article = article_object

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=16)

        pdf.cell(w=0, h=8, txt=f"Receipt no.{self.article.article_id}", align="L", ln=1, border=0)
        pdf.cell(w=0, h=8, txt=f"Article: {self.article.name.title()}", align="L", ln=1, border=0)
        pdf.cell(w=0, h=8, txt=f"Price: {self.article.price} ", align="L", ln=1, border=0)

        pdf.output('receipt.pdf')


# EXECUTION SCRIPT
print(df)

user_choice = input('Enter the article id: ')

article = Articles(user_choice)
article.reduce_stock_by_one()

pdf_receipt = Pdf(article_object=article)
pdf_receipt.generate()









# df = pd.read_csv('hotels.csv')
#
# print(df.loc[df["id"] == 188, "city"].squeeze())












#
# import requests
#
# url = "https://rip.ie/death-notice/s/kerry/killarney?"\
#         "page=1&"\
#         "start=2024-07-08+00%3A00%3A00&"\
#         "end=today&"\
#         "sortField=a.createdAtCastToDate&"\
#         "sortDir=DESC&"\
#         "view=list"
#
#
# response = requests.get(url)
# print(response)
#
# print(response.content)