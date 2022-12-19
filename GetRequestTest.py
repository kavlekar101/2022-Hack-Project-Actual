import requests_html
import json
import requests

payload = {'ICAJAX': '1', 
            'ICNAVTYPEDROPDOWN': '1', 
            'ICType': 'Panel', 
            'ICElementNum': '0', 
            'ICStateNum': '4', 
            'ICAction': 'DERIVED_CLASS_S_SSR_REFRESH_CAL', 
            'ICModelCancel': '0', 
            'ICXPos': '0', 
            'ICYPos': '36', 
            'ResponsetoDiffFrame': '-1', 
            'TargetFrameName': 'None', 
            'FacetPath': 'None', 
            'ICFocus': '', 
            'ICSaveWarningFilter': '0', 
            'ICChanged': '-1', 
            'ICSkipPending': '0', 
            'ICAutoSave': '0', 
            'ICResubmit': '0', 
            'ICSID': 'gDnSQ3J%2FSfhGp33KftbQgB3CIIJ1tuyZK4Au94TUJa8%3D', 
            'ICActionPrompt': 'false', 
            'ICPanelName': '', 
            'ICFind': '', 
            'ICAddCount': '', 
            'ICAppClsData': '', 
            'OSR_DERIVED_RM_FACILITY_ID': 'BE0128', 
            'DERIVED_CLASS_S_START_DT': '11/02/2022', 
            'DERIVED_CLASS_S_MEETING_TIME_START': '8:00AM', 
            'DERIVED_CLASS_S_MEETING_TIME_END': '10:00PM', 
            'OSR_DERIVED_RM_START_DT': '11/01/2022', 
            'OSR_DERIVED_RM_END_DT': '11/01/2022', 
            'DERIVED_CLASS_S_MONDAY_LBL$30$$chk': 'Y', 
            'DERIVED_CLASS_S_MONDAY_LBL$30$': 'Y', 
            'DERIVED_CLASS_S_THURSDAY_LBL$chk': 'Y', 
            'DERIVED_CLASS_S_THURSDAY_LBL': 'Y', 
            'DERIVED_CLASS_S_SUNDAY_LBL$chk': 'Y', 
            'DERIVED_CLASS_S_SUNDAY_LBL': 'Y', 
            'DERIVED_CLASS_S_TUESDAY_LBL$chk': 'Y', 
            'DERIVED_CLASS_S_TUESDAY_LBL': 'Y', 
            'DERIVED_CLASS_S_FRIDAY_LBL$chk': 'Y', 
            'DERIVED_CLASS_S_FRIDAY_LBL': 'Y', 
            'DERIVED_CLASS_S_SHOW_AM_PM$chk': 'Y', 
            'DERIVED_CLASS_S_SHOW_AM_PM': 'Y', 
            'OSR_DERIVED_RM_OSR_SHOW_ROOM$chk': 'Y', 
            'OSR_DERIVED_RM_OSR_SHOW_ROOM': 'Y', 
            'DERIVED_CLASS_S_WEDNESDAY_LBL$chk': 'Y', 
            'DERIVED_CLASS_S_WEDNESDAY_LBL': 'Y', 
            'DERIVED_CLASS_S_SATURDAY_LBL$chk': 'Y', 
            'DERIVED_CLASS_S_SATURDAY_LBL': 'Y', 
            'DERIVED_CLASS_S_SSR_DISP_TITLE$chk': 'N', 
            'OSR_DERIVED_RM_OSR_SHOW_EVENTS$chk': 'Y', 
            'OSR_DERIVED_RM_OSR_SHOW_EVENTS': 'Y',
}

url = "https://courses.osu.edu/psp/csosuct/EMPLOYEE/PUB/c/OSR_CUSTOM_MENU.OSR_ROOM_MATRIX.GBL/post?"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

xml = requests.get("https://courses.osu.edu/psp/csosuct/EMPLOYEE/PUB/c/OSR_CUSTOM_MENU.OSR_ROOM_MATRIX.GBL/post?ICAJAX=1&ICNAVTYPEDROPDOWN=0&ICType=Panel&ICElementNum=0&ICStateNum=2&ICAction=DERIVED_CLASS_S_SSR_REFRESH_CAL&ICModelCancel=0&ICXPos=0&ICYPos=0&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICSkipPending=0&ICAutoSave=0&ICResubmit=0&ICSID=qH%2BToGHdCMZnvER7Bj%2F4YYhVF9igunI9P2fEVDO%2FYxM%3D&ICActionPrompt=false&ICBcDomData=UnknownValue&ICPanelName=&ICFind=&ICAddCount=&ICAppClsData=&OSR_DERIVED_RM_FACILITY_ID=BE0128&DERIVED_CLASS_S_START_DT=11%2F14%2F2022&DERIVED_CLASS_S_MEETING_TIME_START=8%3A00AM&DERIVED_CLASS_S_MEETING_TIME_END=10%3A00PM&OSR_DERIVED_RM_START_DT=11%2F14%2F2022&OSR_DERIVED_RM_END_DT=11%2F14%2F2022&DERIVED_CLASS_S_MONDAY_LBL$30$$chk=Y&DERIVED_CLASS_S_MONDAY_LBL$30$=Y&DERIVED_CLASS_S_THURSDAY_LBL$chk=Y&DERIVED_CLASS_S_THURSDAY_LBL=Y&DERIVED_CLASS_S_SUNDAY_LBL$chk=Y&DERIVED_CLASS_S_SUNDAY_LBL=Y&DERIVED_CLASS_S_TUESDAY_LBL$chk=Y&DERIVED_CLASS_S_TUESDAY_LBL=Y&DERIVED_CLASS_S_FRIDAY_LBL$chk=Y&DERIVED_CLASS_S_FRIDAY_LBL=Y&DERIVED_CLASS_S_SHOW_AM_PM$chk=Y&DERIVED_CLASS_S_SHOW_AM_PM=Y&OSR_DERIVED_RM_OSR_SHOW_ROOM$chk=Y&OSR_DERIVED_RM_OSR_SHOW_ROOM=Y&DERIVED_CLASS_S_WEDNESDAY_LBL$chk=Y&DERIVED_CLASS_S_WEDNESDAY_LBL=Y&DERIVED_CLASS_S_SATURDAY_LBL$chk=Y&DERIVED_CLASS_S_SATURDAY_LBL=Y&DERIVED_CLASS_S_SSR_DISP_TITLE$chk=N&OSR_DERIVED_RM_OSR_SHOW_EVENTS$chk=Y&OSR_DERIVED_RM_OSR_SHOW_EVENTS=Y", headers=headers)


print(xml.text)