import requests
from requests import Session

s = Session()

url = "https://courses.osu.edu/psc/csosuct/EMPLOYEE/PUB/c/OSR_CUSTOM_MENU.OSR_ROOM_MATRIX.GBL?OSR_DERIVED_RM_FACILITY_ID=BE0128&DERIVED_CLASS_S_START_DT=11/02/2022&DERIVED_CLASS_S_MEETING_TIME_START=8:00AM&DERIVED_CLASS_S_MEETING_TIME_END=10:00PM&OSR_DERIVED_RM_START_DT=11/01/2022&OSR_DERIVED_RM_END_DT=11/01/2022"

payload={}
headers = {
  'Cookie': 'ExpirePage=https://courses.osu.edu/psc/csosuct/; PS_DEVICEFEATURES=new:1; PS_LASTSITE=https://courses.osu.edu/psc/csosuct/; PS_LOGINLIST=https://courses.osu.edu/csosuct; PS_TOKEN=rAAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4AgQg4AC4AMQAwABT1tBqGdp6zSne29ltf7oi/8pt+FWwAAAAFAFNkYXRhYHicLYhLDkBAEAXLECewcgcyJj6ZtWCH+KznLO7lcB7RL139qi8giU0U6d6Gb/KehZONnUEbmGRvO0gHZmm2ykZ5oFdbtCe1w+KUguqnFy0tJTWdWNGI9ovX38ID284Oyw==; PS_TOKENEXPIRE=19_Dec_2022_16:47:48_GMT; PS_TokenSite=https://courses.osu.edu/psc/csosuct/?hcwebprd12-15000-PORTAL-PSJSESSIONID; SignOnDefault=; hcwebprd11-15000-PORTAL-PSJSESSIONID=WsIqlq1aPKZAdZ73nsgKctuoJSfPnSBF!-421445930; hcwebprd12-15000-PORTAL-PSJSESSIONID=ChMrSEliJcFgl_vd1D4IwwbZ7E34qe28!-1416440340; NSC_NX-DTPTV-DPVSTFT-TTM-WT=ffffffff839aa4b145525d5f4f58455e445a4a4206ab'
}

response = s.post(url, headers=headers, data=payload)

url = "https://courses.osu.edu/psc/csosuct/EMPLOYEE/PUB/c/OSR_CUSTOM_MENU.OSR_ROOM_MATRIX.GBL/post?ICAJAX=1&ICNAVTYPEDROPDOWN=0&ICType=Panel&ICElementNum=0&ICStateNum=2&ICAction=DERIVED_CLASS_S_SSR_REFRESH_CAL&ICModelCancel=0&ICXPos=0&ICYPos=0&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICSkipPending=0&ICAutoSave=0&ICResubmit=0&ICSID=qH%2BToGHdCMZnvER7Bj%2F4YYhVF9igunI9P2fEVDO%2FYxM%3D&ICActionPrompt=false&ICBcDomData=UnknownValue&ICPanelName=&ICFind=&ICAddCount=&ICAppClsData=&OSR_DERIVED_RM_FACILITY_ID=BE0128&DERIVED_CLASS_S_START_DT=11%2F14%2F2022&DERIVED_CLASS_S_MEETING_TIME_START=8%3A00AM&DERIVED_CLASS_S_MEETING_TIME_END=10%3A00PM&OSR_DERIVED_RM_START_DT=11%2F14%2F2022&OSR_DERIVED_RM_END_DT=11%2F14%2F2022&DERIVED_CLASS_S_MONDAY_LBL$30$$chk=Y&DERIVED_CLASS_S_MONDAY_LBL$30$=Y&DERIVED_CLASS_S_THURSDAY_LBL$chk=Y&DERIVED_CLASS_S_THURSDAY_LBL=Y&DERIVED_CLASS_S_SUNDAY_LBL$chk=Y&DERIVED_CLASS_S_SUNDAY_LBL=Y&DERIVED_CLASS_S_TUESDAY_LBL$chk=Y&DERIVED_CLASS_S_TUESDAY_LBL=Y&DERIVED_CLASS_S_FRIDAY_LBL$chk=Y&DERIVED_CLASS_S_FRIDAY_LBL=Y&DERIVED_CLASS_S_SHOW_AM_PM$chk=Y&DERIVED_CLASS_S_SHOW_AM_PM=Y&OSR_DERIVED_RM_OSR_SHOW_ROOM$chk=Y&OSR_DERIVED_RM_OSR_SHOW_ROOM=Y&DERIVED_CLASS_S_WEDNESDAY_LBL$chk=Y&DERIVED_CLASS_S_WEDNESDAY_LBL=Y&DERIVED_CLASS_S_SATURDAY_LBL$chk=Y&DERIVED_CLASS_S_SATURDAY_LBL=Y&DERIVED_CLASS_S_SSR_DISP_TITLE$chk=N&OSR_DERIVED_RM_OSR_SHOW_EVENTS$chk=Y&OSR_DERIVED_RM_OSR_SHOW_EVENTS=Y"

payload={}
headers = {
  'Cookie': 'ExpirePage=https://courses.osu.edu/psc/csosuct/; PS_DEVICEFEATURES=new:1; PS_LASTSITE=https://courses.osu.edu/psc/csosuct/; PS_LOGINLIST=https://courses.osu.edu/csosuct; PS_TOKEN=rAAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4AgQg4AC4AMQAwABT1tBqGdp6zSne29ltf7oi/8pt+FWwAAAAFAFNkYXRhYHicLYhLDkBAEAXLECewcgcyJj6ZtWCH+KznLO7lcB7RL139qi8giU0U6d6Gb/KehZONnUEbmGRvO0gHZmm2ykZ5oFdbtCe1w+KUguqnFy0tJTWdWNGI9ovX38ID284Oyw==; PS_TOKENEXPIRE=19_Dec_2022_16:47:56_GMT; PS_TokenSite=https://courses.osu.edu/psc/csosuct/?hcwebprd12-15000-PORTAL-PSJSESSIONID; SignOnDefault=; hcwebprd11-15000-PORTAL-PSJSESSIONID=WsIqlq1aPKZAdZ73nsgKctuoJSfPnSBF!-421445930; hcwebprd12-15000-PORTAL-PSJSESSIONID=ChMrSEliJcFgl_vd1D4IwwbZ7E34qe28!-1416440340; NSC_NX-DTPTV-DPVSTFT-TTM-WT=ffffffff839aa4b145525d5f4f58455e445a4a4206ab'
}

response = s.get(url, headers=headers, data=payload)

print(response.text)
