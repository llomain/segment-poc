import settings

adjustInstallAttr = {
  "messageId": "test-message-ltuxbj",
  "timestamp": "2018-10-30T05:55:44.499Z",
  "type": "install attributed",
  "email": "test@example.org",
  "projectId": "PQy9mRAzJu",
  "context": {
      "device": {
        "id": "3e9ffbefafe0d903",
          "type": "Android"
      }},
  "userId": "test-user-nyw3cb",
  "event": "Test Event Name"
}


adjustTrackEvent = {
    "app_token": "4w565xzmb54d",
    "event_token": "f0ob4r",
    "s2s": "1",
    "context": {
      "device": {
        "id": '3e9ffbefafe0d903',
          "type": 'Android'
      },
    },
    "created_at": "0001-01-01T00:00:00Z",
    "device_id": {
        "Adid": "44ae297a759365ca4f8828a616764579",
        "idfa": "D2CADB5F-410F-4963-AC0C-2A78534BDF1E",
        "otherDeviceID": "e3f5536a141811db40efd6400f1d0a4e",
        "otherDeviceID": "660e1d86-6796-463a-be86-897993136018"}
}

individualImageView = {
    'Data': {
        'ClientType': 'Website',
        'EventGeneratedTimestamp': 1519084031683,
        'EventType': 'IndividualImageView',
        'EventVersion': '2.0',
        'MetaData': {
            'AdId': 2012624285,
            'EventProvider': 'desktop-site',
            'EventSource': 'PropertyGallery',
            'IPAddress': '127.0.0.1',
            'ListingStatisticsFactType': '0',
            'ReportingValue': 10,
            'SourceEntityId': '2012624285',
            'SourceEntityType': 'Listing',
            'TargetEntityId': '2012624285',
            'TargetEntityType': 'Listing',
            'UserId': 1234567,
            'UserToken': 'b620383e-9195-481a-8eeb-6f626f816b63'
        }
    },
    'PartitionKey': '1519084031683'
}

# This was initial POC
#kruxDMP = {
#    "EventURL": "https://beacon.krxd.net/event.gif?",
#    "event_id": "LnQCYq9Q",
#    "event_type": "ad",
#    "_kuid": "AAID or IDFA",
#    "testAttribute1": "testValue1",
#    "testAttribute2": "testvalue2", 
#}


kruxTestEvent = {"pixelUrl" : "https://beacon.krxd.net/pixel.gif?",
    #"source" : "smarttag",
    #"fired" : "report",
    #"confid" : "tfx4wayfw",
    "_kpid" : settings.krux_id,
    "_kcp_d" : "z-test-domainMobile",
    "_kcp_s" : "domain.com.au",
    # thing that happened, or section of site
    "_kcp_sc" : "open_app",
    "_kuid" : "Unique Ad ID for User",
    # Page attribute data to send
    "_kpa_domain" : "domain.com.au",
    "_kpa_page.page_info.brand" : "domain",
    "_kpa_page.page_info.generator" : "DO",
    "_kpa_page.page_info.page_id" : "index%20-%20home",
    "_kpa_page.category.sub_category1" : "Index",
    "_kpa_page.category.page_type" : "Homepage",
    # User attribute data to send
    "_kua_kx_lang" : "en-gb",
    "_kua_kx_tech_browser_language" : "en-gb",
    "_kua_kx_geo_country" : "au",
    "_kua_kx_geo_region" : "nsw",   
    "_kua_kx_geo_dma" : "36117",
    # Krux docs state these tech_foo should be on their own but seem to work w the KUA prefix
    "_kua_kx_tech_browser" : "Chrome%2058",
    "_kua_kx_tech_manufacturer" : "Apple%20Inc.",
    "_kua_kx_tech_device" : "Computer",
    "_kua_kx_tech_os" : "Mac%20OS%20X",
    "_kua_kx_whistle" : "0",
    "_kua_profile_id" : "31535446",
    "_kua_aid" : "08021149401725202423114475965021183646",
    "_kua_user.membership_type" : "member",
    "_kua_user.membership_state" : "Logged_in",
    "_knifr" : "9",
    "_kua_kx_tz" : "-660",
    "geo_country" : "au",
    "geo_region" : "nsw", 
    "geo_dma" : "36117",
    "t_navigation_type" : "1",
    "t_dns" : "0",
    "t_tcp" : "0"
    #"t_http_request" : "-1",
    #"t_http_response" : "8",
    #"t_content_ready" : "961",
    #"t_window_load" : "3617",
    #"t_redirect" : "0",
    # Not sure about any of this stuff. 
    #"interchange_ran" : "false",
    #"userdata_was_requested" : "true",
    #"userdata_did_respond" : "true",
    #"store_user_after" : "s64hnl9qb",
    #"store_segs_after" : "swbaidrox%2Cswa99xb4l",
    #"_kurl_" : "https%3A%2F%2Fwww.domain.com.au",
    #"userdata_user" : "MIZNThEx%2Cs64hnl9qb",
    #"userdata_segs" : "swbaidrox%2Cswa99xb4l",
    #"kfuid" : "%22JhiSfh40%22",
    #"kxfp" : "f3ec18ad30dbff5ea7eadbcf7b23c65deadbdd46",
    #"sview" : "2",
    #"kplt0" : "n",
    #"kplt1" : "33644",
    #"kplt2" : "34616",
    #"kplt3" : "35889",
    #"kplt4" : "32604",
    #"kplt5" : "32605",
    #"jsonp_requests" : "https%3A%2F%2Fconsumer.krxd.net%2Fconsent%2Fget%2Fbbb31707-1789-46bd-aff4-6f149795ffba%2C168%2Chttps%3A%2F%2Fbeacon.krxd.net%2Foptout_check%2CNaN%2Chttps%3A%2F%2Fcdn.krxd.net%2Fuserdata%2Fget%2C350"
}


allevents = [adjustTrackEvent, individualImageView, kruxTestEvent]