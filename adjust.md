https://docs.adjust.com/en/event-tracking/#other-device-ids


Parameter name	Example	Content
app_token	4w565xzmb54d	Adjust app token from dashboard
event_token	f0ob4r	Adjust event token from dashboard
s2s	1	has to be set to 1
created_at	2006-01-02T15:04:05Z-0700	Device local time, including timezone
device_id	See Below	Device Identifier(s)

Parameter	Example	Content	Format  
adid	44ae297a759365ca4f8828a616764579	Adjust ID	 
idfa	D2CADB5F-410F-4963-AC0C-2A78534BDF1E	iOS ID for advertisers	With “-“

idfv	EF76726C-D952-451C-8E1A-4E86938BDC20	iOS ID for vendors	With “-“


// Confirm w/ Sam
mac	15118fdce61d	MAC address of device (Android only)	Short, without “:”
mac_md5	e3f5536a141811db40efd6400f1d0a4e	MD5 of MAC (Android only)	Upper case, without “:”
mac_sha1	c1976429369bfe063ed8b3409db7c7e7d87196d9	SHA1 of MAC (Android only)	Upper case, with “:”
android_id	e1cbfb61613b4f50	Android ID	 
gps_adid	660e1d86-6796-463a-be86-897993136018	Google Play advertiser ID	With “-“
win_adid	107e8ea14329d4a2194ebbb6dc0c0fd7	Windows advertising Identifier	 
win_naid	5978aed4-82e5-28cf-8364-dfc64cb1fb84	Windows Phone device ID	With “-“
win_hwid	JKJbFwIArpGAGDmcBTAvlAUMKJkHAMoSCADlJQkDHWG	Windows Phone device ID	 
fire_adid	df07c7dc-cea7-4a89-b328-810ff5acb15d	Amazon Fire advertising ID	With “-“