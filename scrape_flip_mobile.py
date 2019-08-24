import json
from flask import Flask, escape, request, flash
import urllib.request as request

app = Flask(__name__)


@app.route('/scrape_flip_iphone', methods=["POST"])
def scrape_iphone_popular():

    if request.method == "POST":

        brand_error = ""
        attempted_brand = request.form['brand']
        if attempted_brand == "apple":

            filter_error = ''
            attempted_filter = request.form['filter']
            if attempted_filter == "cheapest":

                flash(attempted_brand)
                flash(attempted_filter)

                from urllib.request import urlopen as uReq  # to import web page as html using urllib, opening request as uReq
                from bs4 import BeautifulSoup as soup  # to import beautiful soup as soup

                my_url = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.brand%255B%255D%3DApple&sort=price_asc"

                uclient = uReq(my_url)  # to open the connection, grab the page
                pagehtml = uclient.read()  # to store the page inside page html
                uclient.close()  # to close the connection once the page has read

                name, price, description = [], [], []

                # parsing the html page
                page_soup = soup(pagehtml, "html.parser")

                # finding all div's which contains the class item container which contains each product
                containers = page_soup.findAll("div", {"class": "_1UoZlX"})

                for container in containers:
                    title_container = container.findAll("div", {"class": "_3wU53n"})  # grabbing the name of the product
                    product_name = title_container[0].text
                    name.append(product_name)

                    price_container = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})  # grabbing the price of the product
                    product_price = price_container[0].text
                    price.append(product_price)

                    description_container = container.findAll("div", {"class": "_3ULzGw"})  # grabbing the description of the product
                    product_description = description_container[0].text
                    description.append(product_description)

                product_info_popularity = [{'Product Name': n, 'Product Price': p, 'Product Description': d} for n, p, d in zip(name, price, description)]

                prod_info_popular = json.dumps(product_info_popularity)

                return prod_info_popular

            elif attempted_filter == "newest":

                flash(attempted_brand)
                flash(attempted_filter)

                from urllib.request import urlopen as uReq  # to import web page as html using urllib, opening request as uReq
                from bs4 import BeautifulSoup as soup  # to import beautiful soup as soup

                my_url = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.brand%255B%255D%3DApple&sort=recency_desc"

                uclient = uReq(my_url)  # to open the connection, grab the page
                pagehtml = uclient.read()  # to store the page inside page html
                uclient.close()  # to close the connection once the page has read

                name, price, description = [], [], []

                # parsing the html page
                page_soup = soup(pagehtml, "html.parser")

                # finding all div's which contains the class item container which contains each product
                containers = page_soup.findAll("div", {"class": "_1UoZlX"})

                for container in containers:
                    title_container = container.findAll("div", {"class": "_3wU53n"})  # grabbing the name of the product
                    product_name = title_container[0].text
                    name.append(product_name)

                    price_container = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})  # grabbing the price of the product
                    product_price = price_container[0].text
                    price.append(product_price)

                    description_container = container.findAll("div", {"class": "_3ULzGw"})  # grabbing the description of the product
                    product_description = description_container[0].text
                    description.append(product_description)

                product_info_newest = [{'Product Name': n, 'Product Price': p, 'Product Description': d} for n, p, d in zip(name, price, description)]

                prod_info_newest = json.dumps(product_info_newest)

                return prod_info_newest

            elif attempted_filter == "popular":
                flash(attempted_brand)
                flash(attempted_filter)

                from urllib.request import \
                    urlopen as uReq  # to import web page as html using urllib, opening request as uReq
                from bs4 import BeautifulSoup as soup  # to import beautiful soup as soup

                my_url = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.brand%255B%255D%3DApple"

                uclient = uReq(my_url)  # to open the connection, grab the page
                pagehtml = uclient.read()  # to store the page inside page html
                uclient.close()  # to close the connection once the page has read

                name, price, description = [], [], []

                # parsing the html page
                page_soup = soup(pagehtml, "html.parser")

                # finding all div's which contains the class item container which contains each product
                containers = page_soup.findAll("div", {"class": "_1UoZlX"})

                for container in containers:
                    title_container = container.findAll("div", {"class": "_3wU53n"})  # grabbing the name of the product
                    product_name = title_container[0].text
                    name.append(product_name)

                    price_container = container.findAll("div", {
                        "class": "_1vC4OE _2rQ-NK"})  # grabbing the price of the product
                    product_price = price_container[0].text
                    price.append(product_price)

                    description_container = container.findAll("div", {
                        "class": "_3ULzGw"})  # grabbing the description of the product
                    product_description = description_container[0].text
                    description.append(product_description)

                product_info_newest = [{'Product Name': n, 'Product Price': p, 'Product Description': d} for n, p, d in zip(name, price, description)]

                prod_info_newest = json.dumps(product_info_newest)

                return prod_info_newest

            else:
                filter_error = "Please select filter"
        else:
            brand_error = "Please select brand"


if __name__ == '__main__':
    app.run(debug=True)
