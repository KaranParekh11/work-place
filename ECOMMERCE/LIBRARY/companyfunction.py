import json,datetime
import re
import hashlib
import os
import uuid 
import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/MODELS')
from company import *
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/UTILS')
from test1 import create_database_tabels
from flask import jsonify
import log
import logging

log = logging.getLogger(__name__)

def create_company_info(data1):
    dicth={}
    for (key,value) in data1.items():
        key=key.lower()
        dicth[key]=value
    id=uuid.uuid4().hex
    dh={"id":id}
    dicth.update(dh)
    insert_company_info(dicth)
    log.info("company profile created successfully for company id:"+id)
    return ["Company profile created success fully" , {"company_id":id}],200
    

def deletebyid(id=0):
    # print(id)
    z1=delete_company_info(id)
    # print(z1)
    if z1=="success":
        log.info("company profile deleted successfully for company id:"+id)
        return "deleted succesfully!!!" , 200 
    else:
        log.info("company profile cant delete for company id(invalid company id):"+id)
        return "enter valid company id!!!" , 400

def up_date(id,data2):
    ndicth={}
    for (key,value) in data2.items():
        key=key.lower()
        ndicth[key]=value
    av=update_company_info(id,ndicth)
    if  av == "success":
        log.info("company profile updated successfully for company id:"+id)
        return "company data updated successfully" , 200
    else:
        log.warning("can't update company info for id"+id)
        return "unsuccessful operation for updating company info!!!" , 400
    

def datasearch(args):
    search_dict={}
    for key,value in args.items():
        if value!=None:
            search_dict[key]=value
        else:
            continue
    # print(search_dict)
    if search_dict == {}:
        bn=get_all_company_info()
        return bn,200
    else:
        abcd=search_company(search_dict)
        # print(abcd)
        dict10=[]
        for abc in abcd:
            dict1 ={"id":abc[0],
                "name":abc[1],
                "category":abc[2],
                "website":abc[3],
                "days":abc[4],
                "time":abc[5],
                "address":abc[6]
                }
            dict10.append(dict1)
        # print(dict10)
    log.info('data search done.')
    return dict10,200
        
    
def getall():
    z=get_all_company_info()
    # print(z)
    return z,200
    
def getall_pagination(args):
    offset=args.get("offset")
    limit=args.get("limit")
    if offset!=None and limit!=None and limit!="0":
        offset=int(offset)
        limit=int(limit)
        zx=get_all_company_info()
        # print(zx)
        cx=zx["companies"]
        # print(cx)
        count=len(cx)
        if count%limit==0:
            total_page = count/limit
        else:
            total_page = int(count/limit) + 1

        if offset+1 > total_page:
            A=400
            B="Data not retrieved by user."
            C = "error"
            D = False 
        else:
            A=200
            B="Data retrieved by user." 
            D = True 
            ab=[]
            page_no=offset+1
            data_limit_end = page_no*limit
            data_limit_start=data_limit_end - limit
            for a in range(data_limit_start,data_limit_end):
                if a==count:
                    break
                ab.append(cx[a])
               
            C= {"companies":ab}
            # print(C)


        xyz = {
                "Statuscode":A,
                "message":B,
                "data":C,
                "success":D,
                "count":count,
                "Total page":int(total_page)
              }
        log.info("pagination done for offset:"+str(offset)+"limit"+str(limit))
        return xyz,200
    else:
        log.warning("Enter valid offset and limit value!!!for pagination")
        return "Enter valid offset and limit value!!!",400

def getbyid(id):
    abc = get_data_by_id(id)
    if abc!="error":
        dict10 ={"id":abc[0],
            "name":abc[1],
            "category":abc[2],
            "website":abc[3],
            "days":abc[4],
            "time":abc[5],
            "address":abc[6]
            }
        log.info("data retriev for id"+id)
        return dict10 , 200
    else:
        return "enter valid user id!!!" , 401

def checkput(data1):
    list1=[]
    v=0
    for i in data1.keys():
        list1.append(i)
    l2=['category','name','website','days','time','address']
    for i in list1:
        if i in l2:
            v="success"
            continue
        else:
            v=0
            break
    return v
    
    
    




