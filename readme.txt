Super user-
username- Sandhiya@123
password- Sandhiya@123

Registration- 
GET_ALL- http://127.0.0.1:8000/reg/
POST- http://127.0.0.1:8000/reg/


Login-
Get_Id= http://127.0.0.1:8000/login/<phonenumber>/
put_Id= http://127.0.0.1:8000/login/<phonenumber>/ -- also send the data in json format with it-example-  {
        "phonenumber": "983354321",
        "firstname": "none",
        "lastname": "changed",
        "role": "Partner",
        "attendance": 0,
        "foodcounter": 0
    }
delete_Id= http://127.0.0.1:8000/login/<phonenumber>/


Deployed on: https://sandhiyaacharya.pythonanywhere.com/