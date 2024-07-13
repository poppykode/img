# Generated by Django 5.0.3 on 2024-07-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_studybuddyadditionalinfo_availability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaladditionalinfo',
            name='time_zone',
            field=models.CharField(choices=[('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('MET', 'MET'), ('Asia/Amman', 'Asia/Amman'), ('Turkey', 'Turkey'), ('Europe/Vienna', 'Europe/Vienna'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Indian/Maldives', 'Indian/Maldives'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Africa/Kampala', 'Africa/Kampala'), ('America/Montserrat', 'America/Montserrat'), ('Asia/Damascus', 'Asia/Damascus'), ('America/Halifax', 'America/Halifax'), ('America/Bogota', 'America/Bogota'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Europe/Monaco', 'Europe/Monaco'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Etc/GMT+11', 'Etc/GMT+11'), ('EST5EDT', 'EST5EDT'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Asia/Hebron', 'Asia/Hebron'), ('Australia/Sydney', 'Australia/Sydney'), ('MST7MDT', 'MST7MDT'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('America/Cordoba', 'America/Cordoba'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Africa/Asmara', 'Africa/Asmara'), ('Australia/Tasmania', 'Australia/Tasmania'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Eire', 'Eire'), ('Etc/Universal', 'Etc/Universal'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('America/Cayenne', 'America/Cayenne'), ('America/Porto_Acre', 'America/Porto_Acre'), ('America/Moncton', 'America/Moncton'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Etc/GMT-14', 'Etc/GMT-14'), ('CET', 'CET'), ('Singapore', 'Singapore'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Asia/Kabul', 'Asia/Kabul'), ('GB', 'GB'), ('Asia/Brunei', 'Asia/Brunei'), ('Africa/Niamey', 'Africa/Niamey'), ('Libya', 'Libya'), ('UCT', 'UCT'), ('GMT-0', 'GMT-0'), ('Europe/Oslo', 'Europe/Oslo'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Australia/Queensland', 'Australia/Queensland'), ('Europe/Madrid', 'Europe/Madrid'), ('Asia/Macao', 'Asia/Macao'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('PRC', 'PRC'), ('America/Whitehorse', 'America/Whitehorse'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Asia/Saigon', 'Asia/Saigon'), ('America/Toronto', 'America/Toronto'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Zulu', 'Zulu'), ('Europe/Minsk', 'Europe/Minsk'), ('Mexico/General', 'Mexico/General'), ('America/Belem', 'America/Belem'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Colombo', 'Asia/Colombo'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('America/Resolute', 'America/Resolute'), ('US/Arizona', 'US/Arizona'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Africa/Blantyre', 'Africa/Blantyre'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Asia/Harbin', 'Asia/Harbin'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('GMT0', 'GMT0'), ('ROC', 'ROC'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Scoresbysund', 'America/Scoresbysund'), ('America/Creston', 'America/Creston'), ('America/Managua', 'America/Managua'), ('Africa/Maputo', 'Africa/Maputo'), ('America/Nassau', 'America/Nassau'), ('NZ', 'NZ'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Edmonton', 'America/Edmonton'), ('America/Cancun', 'America/Cancun'), ('America/Dawson', 'America/Dawson'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Lima', 'America/Lima'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/Santarem', 'America/Santarem'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Japan', 'Japan'), ('Indian/Christmas', 'Indian/Christmas'), ('America/Metlakatla', 'America/Metlakatla'), ('MST', 'MST'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Africa/Kigali', 'Africa/Kigali'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Cuiaba', 'America/Cuiaba'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Pacific/Niue', 'Pacific/Niue'), ('America/Recife', 'America/Recife'), ('Iceland', 'Iceland'), ('America/Chicago', 'America/Chicago'), ('US/Alaska', 'US/Alaska'), ('Australia/NSW', 'Australia/NSW'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Africa/Djibouti', 'Africa/Djibouti'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/Winnipeg', 'America/Winnipeg'), ('Jamaica', 'Jamaica'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Africa/Douala', 'Africa/Douala'), ('America/Barbados', 'America/Barbados'), ('America/Guyana', 'America/Guyana'), ('America/Menominee', 'America/Menominee'), ('Pacific/Palau', 'Pacific/Palau'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Asia/Beirut', 'Asia/Beirut'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/Mazatlan', 'America/Mazatlan'), ('America/Indianapolis', 'America/Indianapolis'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('America/Swift_Current', 'America/Swift_Current'), ('Indian/Comoro', 'Indian/Comoro'), ('Europe/Riga', 'Europe/Riga'), ('Europe/Moscow', 'Europe/Moscow'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Jujuy', 'America/Jujuy'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Shiprock', 'America/Shiprock'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Europe/Vatican', 'Europe/Vatican'), ('America/Boise', 'America/Boise'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Africa/Lagos', 'Africa/Lagos'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Australia/Brisbane', 'Australia/Brisbane'), ('America/Tortola', 'America/Tortola'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Asia/Taipei', 'Asia/Taipei'), ('Etc/GMT-6', 'Etc/GMT-6'), ('America/Montreal', 'America/Montreal'), ('America/Antigua', 'America/Antigua'), ('Africa/Asmera', 'Africa/Asmera'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Europe/Dublin', 'Europe/Dublin'), ('America/St_Johns', 'America/St_Johns'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Europe/Guernsey', 'Europe/Guernsey'), ('America/Juneau', 'America/Juneau'), ('America/Catamarca', 'America/Catamarca'), ('GMT', 'GMT'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Canada/Yukon', 'Canada/Yukon'), ('Etc/GMT0', 'Etc/GMT0'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Egypt', 'Egypt'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Europe/Volgograd', 'Europe/Volgograd'), ('America/Fortaleza', 'America/Fortaleza'), ('Pacific/Ponape', 'Pacific/Ponape'), ('US/Hawaii', 'US/Hawaii'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Asia/Seoul', 'Asia/Seoul'), ('US/Samoa', 'US/Samoa'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Asia/Muscat', 'Asia/Muscat'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Indian/Mahe', 'Indian/Mahe'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('America/Regina', 'America/Regina'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('America/Guadeloupe', 'America/Guadeloupe'), ('America/Nome', 'America/Nome'), ('Israel', 'Israel'), ('Australia/South', 'Australia/South'), ('Asia/Makassar', 'Asia/Makassar'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Australia/Perth', 'Australia/Perth'), ('America/Marigot', 'America/Marigot'), ('Atlantic/Canary', 'Atlantic/Canary'), ('NZ-CHAT', 'NZ-CHAT'), ('America/Mexico_City', 'America/Mexico_City'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Asia/Omsk', 'Asia/Omsk'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Asia/Oral', 'Asia/Oral'), ('Asia/Anadyr', 'Asia/Anadyr'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Asia/Tokyo', 'Asia/Tokyo'), ('America/Iqaluit', 'America/Iqaluit'), ('Europe/Samara', 'Europe/Samara'), ('America/Curacao', 'America/Curacao'), ('Asia/Katmandu', 'Asia/Katmandu'), ('America/Panama', 'America/Panama'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Africa/Malabo', 'Africa/Malabo'), ('Pacific/Efate', 'Pacific/Efate'), ('America/Araguaina', 'America/Araguaina'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Asia/Dubai', 'Asia/Dubai'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('US/East-Indiana', 'US/East-Indiana'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('WET', 'WET'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Etc/GMT+8', 'Etc/GMT+8'), ('EET', 'EET'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Asia/Karachi', 'Asia/Karachi'), ('Europe/Vilnius', 'Europe/Vilnius'), ('America/Grenada', 'America/Grenada'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Europe/Belfast', 'Europe/Belfast'), ('Europe/Jersey', 'Europe/Jersey'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Europe/London', 'Europe/London'), ('Africa/Libreville', 'Africa/Libreville'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Etc/GMT+1', 'Etc/GMT+1'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Canada/Mountain', 'Canada/Mountain'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Navajo', 'Navajo'), ('Pacific/Easter', 'Pacific/Easter'), ('Europe/Budapest', 'Europe/Budapest'), ('Australia/Darwin', 'Australia/Darwin'), ('Australia/LHI', 'Australia/LHI'), ('America/Anguilla', 'America/Anguilla'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/St_Vincent', 'America/St_Vincent'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('America/Matamoros', 'America/Matamoros'), ('Asia/Yangon', 'Asia/Yangon'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Sitka', 'America/Sitka'), ('Asia/Macau', 'Asia/Macau'), ('US/Pacific', 'US/Pacific'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Canada/Pacific', 'Canada/Pacific'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/Inuvik', 'America/Inuvik'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Etc/Zulu', 'Etc/Zulu'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Europe/Malta', 'Europe/Malta'), ('Australia/Canberra', 'Australia/Canberra'), ('Europe/Chisinau', 'Europe/Chisinau'), ('America/Martinique', 'America/Martinique'), ('America/Jamaica', 'America/Jamaica'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Asia/Qatar', 'Asia/Qatar'), ('Australia/Hobart', 'Australia/Hobart'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Australia/North', 'Australia/North'), ('US/Eastern', 'US/Eastern'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('America/Manaus', 'America/Manaus'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Caracas', 'America/Caracas'), ('America/Atikokan', 'America/Atikokan'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('America/Rainy_River', 'America/Rainy_River'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Australia/Eucla', 'Australia/Eucla'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Yakutat', 'America/Yakutat'), ('UTC', 'UTC'), ('Africa/Monrovia', 'Africa/Monrovia'), ('ROK', 'ROK'), ('America/Lower_Princes', 'America/Lower_Princes'), ('America/Vancouver', 'America/Vancouver'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Mendoza', 'America/Mendoza'), ('GB-Eire', 'GB-Eire'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Asia/Almaty', 'Asia/Almaty'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Africa/Conakry', 'Africa/Conakry'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Asia/Magadan', 'Asia/Magadan'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('America/Maceio', 'America/Maceio'), ('US/Michigan', 'US/Michigan'), ('America/Nipigon', 'America/Nipigon'), ('Brazil/East', 'Brazil/East'), ('US/Central', 'US/Central'), ('Africa/Maseru', 'Africa/Maseru'), ('America/Ojinaga', 'America/Ojinaga'), ('Europe/Berlin', 'Europe/Berlin'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Chile/Continental', 'Chile/Continental'), ('Pacific/Guam', 'Pacific/Guam'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('America/Dominica', 'America/Dominica'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Africa/Harare', 'Africa/Harare'), ('Africa/Banjul', 'Africa/Banjul'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Asia/Chita', 'Asia/Chita'), ('Etc/UTC', 'Etc/UTC'), ('Asia/Tehran', 'Asia/Tehran'), ('America/Monterrey', 'America/Monterrey'), ('Brazil/West', 'Brazil/West'), ('Canada/Central', 'Canada/Central'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Brazil/Acre', 'Brazil/Acre'), ('Australia/Victoria', 'Australia/Victoria'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Africa/Juba', 'Africa/Juba'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Europe/Kirov', 'Europe/Kirov'), ('America/Detroit', 'America/Detroit'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('America/Havana', 'America/Havana'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Australia/Lindeman', 'Australia/Lindeman'), ('GMT+0', 'GMT+0'), ('America/Rosario', 'America/Rosario'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Ensenada', 'America/Ensenada'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Asia/Dacca', 'Asia/Dacca'), ('Africa/Tripoli', 'Africa/Tripoli'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Africa/Bamako', 'Africa/Bamako'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Africa/Dakar', 'Africa/Dakar'), ('America/St_Kitts', 'America/St_Kitts'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('America/Costa_Rica', 'America/Costa_Rica'), ('America/Virgin', 'America/Virgin'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Australia/West', 'Australia/West'), ('Pacific/Truk', 'Pacific/Truk'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/New_York', 'America/New_York'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Miquelon', 'America/Miquelon'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Tijuana', 'America/Tijuana'), ('America/Atka', 'America/Atka'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Pacific/Midway', 'Pacific/Midway'), ('US/Mountain', 'US/Mountain'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Europe/Zurich', 'Europe/Zurich'), ('America/El_Salvador', 'America/El_Salvador'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Etc/GMT', 'Etc/GMT'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Universal', 'Universal'), ('America/Denver', 'America/Denver'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Asia/Manila', 'Asia/Manila'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Asia/Atyrau', 'Asia/Atyrau'), ('America/Aruba', 'America/Aruba'), ('Europe/Tirane', 'Europe/Tirane'), ('Asia/Baku', 'Asia/Baku'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Australia/Currie', 'Australia/Currie'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Hongkong', 'Hongkong'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('America/St_Lucia', 'America/St_Lucia'), ('Europe/Brussels', 'Europe/Brussels'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Cuba', 'Cuba'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Asia/Hovd', 'Asia/Hovd'), ('Europe/Rome', 'Europe/Rome'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Asia/Kuching', 'Asia/Kuching'), ('Pacific/Apia', 'Pacific/Apia'), ('America/Noronha', 'America/Noronha'), ('Europe/Kyiv', 'Europe/Kyiv'), ('America/Belize', 'America/Belize'), ('Greenwich', 'Greenwich'), ('Europe/Busingen', 'Europe/Busingen'), ('Asia/Singapore', 'Asia/Singapore'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Africa/Freetown', 'Africa/Freetown'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/Asuncion', 'America/Asuncion'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Africa/Accra', 'Africa/Accra'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('America/Bahia', 'America/Bahia'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Kwajalein', 'Kwajalein'), ('Etc/GMT-11', 'Etc/GMT-11'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Asia/Jakarta', 'Asia/Jakarta'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Asia/Aden', 'Asia/Aden'), ('Europe/Paris', 'Europe/Paris'), ('Africa/Abidjan', 'Africa/Abidjan'), ('America/St_Thomas', 'America/St_Thomas'), ('EST', 'EST'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Pacific/Yap', 'Pacific/Yap'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Europe/Sofia', 'Europe/Sofia'), ('America/Eirunepe', 'America/Eirunepe'), ('Europe/Prague', 'Europe/Prague'), ('US/Aleutian', 'US/Aleutian'), ('America/Goose_Bay', 'America/Goose_Bay'), ('America/La_Paz', 'America/La_Paz'), ('Asia/Dili', 'Asia/Dili'), ('PST8PDT', 'PST8PDT'), ('America/Paramaribo', 'America/Paramaribo'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Australia/ACT', 'Australia/ACT'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('HST', 'HST'), ('America/Adak', 'America/Adak'), ('Africa/Bissau', 'Africa/Bissau'), ('Antarctica/Davis', 'Antarctica/Davis'), ('W-SU', 'W-SU'), ('Africa/Cairo', 'Africa/Cairo'), ('Canada/Eastern', 'Canada/Eastern'), ('Europe/Simferopol', 'Europe/Simferopol'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('America/Cayman', 'America/Cayman'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Pacific/Wake', 'Pacific/Wake'), ('Europe/Athens', 'Europe/Athens'), ('Portugal', 'Portugal'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('America/Nuuk', 'America/Nuuk'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Indian/Reunion', 'Indian/Reunion'), ('America/Anchorage', 'America/Anchorage'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('America/Guatemala', 'America/Guatemala'), ('Europe/Andorra', 'Europe/Andorra'), ('Europe/Saratov', 'Europe/Saratov'), ('Asia/Bangkok', 'Asia/Bangkok'), ('America/Godthab', 'America/Godthab'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Phoenix', 'America/Phoenix'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Louisville', 'America/Louisville'), ('America/Kralendijk', 'America/Kralendijk'), ('Africa/Algiers', 'Africa/Algiers'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Poland', 'Poland'), ('America/Merida', 'America/Merida'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Iran', 'Iran'), ('America/Montevideo', 'America/Montevideo'), ('Etc/UCT', 'Etc/UCT'), ('Africa/Lome', 'Africa/Lome'), ('America/Yellowknife', 'America/Yellowknife'), ('Europe/Skopje', 'Europe/Skopje'), ('CST6CDT', 'CST6CDT'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Pacific/Auckland', 'Pacific/Auckland'), ('America/Santiago', 'America/Santiago'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Africa/Tunis', 'Africa/Tunis'), ('Europe/Kiev', 'Europe/Kiev'), ('America/Thule', 'America/Thule'), ('America/Glace_Bay', 'America/Glace_Bay')], max_length=255),
        ),
    ]