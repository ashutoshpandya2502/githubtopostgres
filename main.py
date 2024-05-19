import requests


import json

def call_api(url:str)->dict:
    response=requests.get(url)
    return  response.json()
def save_data_as_json(file_name:str,userdict:dict)->str:
    with open(f'{file_name}.json', 'w') as fp:
        json.dump(userdict, fp)
    return f"saved '{file_name}.json"


def transform_data(username:str)->str:
    url_with_username=f"https://api.github.com/users/{username}/repos"
    print(url_with_username)
    response=call_api(url_with_username)
    userdict={}
    userdata_list=[]
    for data in response:
        data_dict={}
        data_dict["id"] =data.get('id',None)
        data_dict["full_name"] = data.get('full_name', None)
        data_dict["repo_name"] = data.get('name', None)
        data_dict["owner_login"] = data.get('owner',dict).get('login', None)
        data_dict["created_at"] = data.get('created_at', None)
        data_dict["updated_at"] = data.get('updated_at', None)
        data_dict["pushed_at"] = data.get('pushed_at', None)
        data_dict["git_url"] = data.get('git_url', None)
        data_dict["open_issues_count"]=data.get('open_issues_count', None)
        data_dict["visibility"]=data.get('visibility')
        userdata_list.append(data_dict)
    userdict[f"{username}"]=userdata_list
    print(save_data_as_json(username,userdict))



if __name__ == '__main__':
    list_of_username=['mralexgray']
    for username in list_of_username:
        transform_data(username)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
