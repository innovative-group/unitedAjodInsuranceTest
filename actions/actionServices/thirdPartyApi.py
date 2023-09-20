import os;
from dotenv import load_dotenv, find_dotenv
from actions.actionServices.httpApi import http_get;
load_dotenv(find_dotenv());

#Api credetials
API_BASE_URL = os.getenv('API_BASE_URL');
headers = {'content-type': 'application/json'};



def Branchlist():
    print("hello")
    url = f"{API_BASE_URL}/GetBranchList";
    response=http_get(url,headers)
    return response


def serviceCharge(services,searchQuery,language_id):
    url= f"{API_BASE_URL}{services}?search={searchQuery}&language_id={language_id}"
    print(url,"bot url")
    response= http_get(url)
    return response


def getProductByCatagories(searchQuery,language_id):
    url= f"{API_BASE_URL}allProducts/bycatagories?search={searchQuery}&language_id={language_id}"
    print(url,"bot url")
    response= http_get(url)
    return response


def getProductCatagories(language_id):
    url= f"{API_BASE_URL}product/catagories?language_id={language_id}"
    print(url,"bot url")
    response= http_get(url)
    return response


def getProductByNameAndType(type,searchQuery,language_id):
    url=f"{API_BASE_URL}allProducts?search={searchQuery}&language_id={language_id}"
    if type:
        url= f"{API_BASE_URL}allProducts?search={searchQuery}&language_id={language_id}&type={type}"
    else:
      url= f"{API_BASE_URL}allProducts?search={searchQuery}&language_id={language_id}"  
    if searchQuery=="woman":
        query_one='Nari Samman Bachat Khata';
        query_two='Women Special Saving';
        url= f"{API_BASE_URL}allProducts?language_id={language_id}&search={query_one}&search={query_two}" 
    if searchQuery=="chhori":
        query_one='chhori surakshya bachat khata';
        query_two='chhori beti kalyan bachat khata';
        url= f"{API_BASE_URL}allProducts?language_id={language_id}&search={query_one}&search={query_two}" 
    response= http_get(url)
    return response

def getInterestRate(type,searchQuery,language_id):
    url= f"{API_BASE_URL}interestRate?search={searchQuery}&language_id={language_id}"
    if type=='loan':
        url= f"{API_BASE_URL}interestRateOnLoan?search={searchQuery}&language_id={language_id}"
        print(url,"response rll")
    else:   
         url= f"{API_BASE_URL}interestRate?search={searchQuery}&language_id={language_id}"
    response= http_get(url)
    return response

def office_bankingHour(language_id):
    url= f"{API_BASE_URL}office_bankingHour?language_id={language_id}"
    response= http_get(url)
    return response

def loan(language_id,searchQuery):
    url= f"{API_BASE_URL}loan?language_id={language_id}&search={searchQuery}"
    response= http_get(url)
    return response

def loanWithTitle(language_id,searchQuery):
    url= f"{API_BASE_URL}loan/type?language_id={language_id}&search={searchQuery}"
    response= http_get(url)
    return response