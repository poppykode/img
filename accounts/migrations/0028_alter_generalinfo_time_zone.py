# Generated by Django 5.0.3 on 2024-08-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_alter_generalinfo_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='time_zone',
            field=models.CharField(choices=[('America/Danmarkshavn', 'America/Danmarkshavn'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Africa/Algiers', 'Africa/Algiers'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Jujuy', 'America/Jujuy'), ('Etc/GMT+4', 'Etc/GMT+4'), ('US/Pacific', 'US/Pacific'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Asia/Damascus', 'Asia/Damascus'), ('NZ-CHAT', 'NZ-CHAT'), ('Asia/Almaty', 'Asia/Almaty'), ('US/Arizona', 'US/Arizona'), ('Europe/Nicosia', 'Europe/Nicosia'), ('US/Eastern', 'US/Eastern'), ('Europe/Sofia', 'Europe/Sofia'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('America/Chicago', 'America/Chicago'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Africa/Niamey', 'Africa/Niamey'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Asia/Baku', 'Asia/Baku'), ('Asia/Chungking', 'Asia/Chungking'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Israel', 'Israel'), ('Japan', 'Japan'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Pacific/Majuro', 'Pacific/Majuro'), ('MET', 'MET'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('America/Santarem', 'America/Santarem'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Europe/Prague', 'Europe/Prague'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('America/Whitehorse', 'America/Whitehorse'), ('Australia/ACT', 'Australia/ACT'), ('US/Alaska', 'US/Alaska'), ('Asia/Gaza', 'Asia/Gaza'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Europe/Andorra', 'Europe/Andorra'), ('Europe/Brussels', 'Europe/Brussels'), ('Pacific/Guam', 'Pacific/Guam'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Cuiaba', 'America/Cuiaba'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/Guyana', 'America/Guyana'), ('America/Godthab', 'America/Godthab'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Asia/Chongqing', 'Asia/Chongqing'), ('America/Noronha', 'America/Noronha'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Africa/Kigali', 'Africa/Kigali'), ('Australia/West', 'Australia/West'), ('America/Cordoba', 'America/Cordoba'), ('Africa/Bamako', 'Africa/Bamako'), ('Africa/Asmera', 'Africa/Asmera'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Pacific/Noumea', 'Pacific/Noumea'), ('US/Aleutian', 'US/Aleutian'), ('Africa/Djibouti', 'Africa/Djibouti'), ('US/Hawaii', 'US/Hawaii'), ('Europe/Vilnius', 'Europe/Vilnius'), ('America/Atka', 'America/Atka'), ('Australia/North', 'Australia/North'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Asia/Aden', 'Asia/Aden'), ('Africa/Gaborone', 'Africa/Gaborone'), ('America/Nome', 'America/Nome'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('America/Hermosillo', 'America/Hermosillo'), ('Iceland', 'Iceland'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Catamarca', 'America/Catamarca'), ('Pacific/Easter', 'Pacific/Easter'), ('Africa/Douala', 'Africa/Douala'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Indian/Christmas', 'Indian/Christmas'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('America/Phoenix', 'America/Phoenix'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Egypt', 'Egypt'), ('Libya', 'Libya'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/Lower_Princes', 'America/Lower_Princes'), ('America/St_Kitts', 'America/St_Kitts'), ('Europe/Kirov', 'Europe/Kirov'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('America/Cayenne', 'America/Cayenne'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Asia/Chita', 'Asia/Chita'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Africa/Maseru', 'Africa/Maseru'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Indian/Reunion', 'Indian/Reunion'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Canada/Atlantic', 'Canada/Atlantic'), ('ROK', 'ROK'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('America/Paramaribo', 'America/Paramaribo'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Grenada', 'America/Grenada'), ('America/St_Lucia', 'America/St_Lucia'), ('America/Moncton', 'America/Moncton'), ('Europe/Zagreb', 'Europe/Zagreb'), ('US/Samoa', 'US/Samoa'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Boise', 'America/Boise'), ('Canada/Pacific', 'Canada/Pacific'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Africa/Harare', 'Africa/Harare'), ('WET', 'WET'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Europe/Belfast', 'Europe/Belfast'), ('Asia/Singapore', 'Asia/Singapore'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Europe/Madrid', 'Europe/Madrid'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Asia/Karachi', 'Asia/Karachi'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Brazil/East', 'Brazil/East'), ('Europe/Tirane', 'Europe/Tirane'), ('Etc/GMT+6', 'Etc/GMT+6'), ('America/Havana', 'America/Havana'), ('America/Grand_Turk', 'America/Grand_Turk'), ('America/Recife', 'America/Recife'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('GMT0', 'GMT0'), ('Africa/Maputo', 'Africa/Maputo'), ('Asia/Dubai', 'Asia/Dubai'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('America/Mazatlan', 'America/Mazatlan'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('America/La_Paz', 'America/La_Paz'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Europe/Saratov', 'Europe/Saratov'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Cancun', 'America/Cancun'), ('GB-Eire', 'GB-Eire'), ('America/Nassau', 'America/Nassau'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Asia/Macao', 'Asia/Macao'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Managua', 'America/Managua'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('W-SU', 'W-SU'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Asia/Hovd', 'Asia/Hovd'), ('Australia/South', 'Australia/South'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Europe/Dublin', 'Europe/Dublin'), ('America/Belem', 'America/Belem'), ('Asia/Harbin', 'Asia/Harbin'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Europe/Malta', 'Europe/Malta'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Asia/Manila', 'Asia/Manila'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Australia/Tasmania', 'Australia/Tasmania'), ('America/Maceio', 'America/Maceio'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Portugal', 'Portugal'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Europe/Kiev', 'Europe/Kiev'), ('Pacific/Efate', 'Pacific/Efate'), ('America/Edmonton', 'America/Edmonton'), ('UTC', 'UTC'), ('America/Eirunepe', 'America/Eirunepe'), ('America/Kralendijk', 'America/Kralendijk'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/St_Thomas', 'America/St_Thomas'), ('Singapore', 'Singapore'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Bogota', 'America/Bogota'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('America/Yakutat', 'America/Yakutat'), ('Indian/Comoro', 'Indian/Comoro'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Araguaina', 'America/Araguaina'), ('Asia/Saigon', 'Asia/Saigon'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Europe/Samara', 'Europe/Samara'), ('US/Mountain', 'US/Mountain'), ('America/Rosario', 'America/Rosario'), ('NZ', 'NZ'), ('America/St_Vincent', 'America/St_Vincent'), ('Europe/Helsinki', 'Europe/Helsinki'), ('America/Rainy_River', 'America/Rainy_River'), ('America/Bahia', 'America/Bahia'), ('America/Monterrey', 'America/Monterrey'), ('America/Ojinaga', 'America/Ojinaga'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('EST5EDT', 'EST5EDT'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('America/Guatemala', 'America/Guatemala'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Europe/Moscow', 'Europe/Moscow'), ('Brazil/Acre', 'Brazil/Acre'), ('Brazil/West', 'Brazil/West'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Asia/Seoul', 'Asia/Seoul'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Europe/Vaduz', 'Europe/Vaduz'), ('CST6CDT', 'CST6CDT'), ('America/Swift_Current', 'America/Swift_Current'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('US/Michigan', 'US/Michigan'), ('America/Atikokan', 'America/Atikokan'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Pacific/Palau', 'Pacific/Palau'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Europe/London', 'Europe/London'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Australia/LHI', 'Australia/LHI'), ('America/Virgin', 'America/Virgin'), ('America/Louisville', 'America/Louisville'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Australia/Currie', 'Australia/Currie'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Pacific/Kanton', 'Pacific/Kanton'), ('America/Barbados', 'America/Barbados'), ('Asia/Makassar', 'Asia/Makassar'), ('Canada/Yukon', 'Canada/Yukon'), ('Africa/Bissau', 'Africa/Bissau'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Metlakatla', 'America/Metlakatla'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Europe/Vatican', 'Europe/Vatican'), ('Universal', 'Universal'), ('America/Jamaica', 'America/Jamaica'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('America/Caracas', 'America/Caracas'), ('Australia/Queensland', 'Australia/Queensland'), ('Africa/Blantyre', 'Africa/Blantyre'), ('America/St_Johns', 'America/St_Johns'), ('Asia/Qatar', 'Asia/Qatar'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('ROC', 'ROC'), ('Asia/Jakarta', 'Asia/Jakarta'), ('America/Tortola', 'America/Tortola'), ('US/East-Indiana', 'US/East-Indiana'), ('Europe/Chisinau', 'Europe/Chisinau'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Asia/Colombo', 'Asia/Colombo'), ('America/Panama', 'America/Panama'), ('Africa/Lagos', 'Africa/Lagos'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Etc/UTC', 'Etc/UTC'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Pacific/Wake', 'Pacific/Wake'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Africa/Conakry', 'Africa/Conakry'), ('America/Anchorage', 'America/Anchorage'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Europe/Budapest', 'Europe/Budapest'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('America/Mendoza', 'America/Mendoza'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Canada/Central', 'Canada/Central'), ('EET', 'EET'), ('Pacific/Apia', 'Pacific/Apia'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Asia/Omsk', 'Asia/Omsk'), ('GMT+0', 'GMT+0'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Pacific/Nauru', 'Pacific/Nauru'), ('MST7MDT', 'MST7MDT'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Nuuk', 'America/Nuuk'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Europe/Lisbon', 'Europe/Lisbon'), ('America/Belize', 'America/Belize'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Asia/Brunei', 'Asia/Brunei'), ('Indian/Maldives', 'Indian/Maldives'), ('Poland', 'Poland'), ('Canada/Mountain', 'Canada/Mountain'), ('Australia/Sydney', 'Australia/Sydney'), ('America/Merida', 'America/Merida'), ('America/Matamoros', 'America/Matamoros'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/Curacao', 'America/Curacao'), ('Eire', 'Eire'), ('America/Lima', 'America/Lima'), ('Asia/Dili', 'Asia/Dili'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Amman', 'Asia/Amman'), ('Etc/Universal', 'Etc/Universal'), ('America/Resolute', 'America/Resolute'), ('HST', 'HST'), ('Europe/Paris', 'Europe/Paris'), ('Asia/Kashgar', 'Asia/Kashgar'), ('PRC', 'PRC'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Etc/UCT', 'Etc/UCT'), ('Europe/Skopje', 'Europe/Skopje'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Mexico/General', 'Mexico/General'), ('Europe/Rome', 'Europe/Rome'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Europe/Busingen', 'Europe/Busingen'), ('US/Central', 'US/Central'), ('America/Detroit', 'America/Detroit'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Australia/Hobart', 'Australia/Hobart'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Asia/Muscat', 'Asia/Muscat'), ('America/Martinique', 'America/Martinique'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Africa/Cairo', 'Africa/Cairo'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Australia/Adelaide', 'Australia/Adelaide'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('America/Manaus', 'America/Manaus'), ('Europe/Volgograd', 'Europe/Volgograd'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('GMT-0', 'GMT-0'), ('America/Montreal', 'America/Montreal'), ('Asia/Dacca', 'Asia/Dacca'), ('Asia/Hebron', 'Asia/Hebron'), ('America/Asuncion', 'America/Asuncion'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Zulu', 'Zulu'), ('America/Juneau', 'America/Juneau'), ('Chile/Continental', 'Chile/Continental'), ('America/Tijuana', 'America/Tijuana'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Hongkong', 'Hongkong'), ('Indian/Chagos', 'Indian/Chagos'), ('Canada/Eastern', 'Canada/Eastern'), ('Africa/Asmara', 'Africa/Asmara'), ('Australia/Canberra', 'Australia/Canberra'), ('Africa/Lome', 'Africa/Lome'), ('Australia/NSW', 'Australia/NSW'), ('Navajo', 'Navajo'), ('Asia/Oral', 'Asia/Oral'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Pacific/Niue', 'Pacific/Niue'), ('Etc/GMT', 'Etc/GMT'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Europe/Minsk', 'Europe/Minsk'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('CET', 'CET'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Asia/Macau', 'Asia/Macau'), ('GMT', 'GMT'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Costa_Rica', 'America/Costa_Rica'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Australia/Eucla', 'Australia/Eucla'), ('America/Guayaquil', 'America/Guayaquil'), ('Asia/Kuching', 'Asia/Kuching'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Europe/Berlin', 'Europe/Berlin'), ('Africa/Malabo', 'Africa/Malabo'), ('Cuba', 'Cuba'), ('America/Los_Angeles', 'America/Los_Angeles'), ('America/Aruba', 'America/Aruba'), ('Pacific/Saipan', 'Pacific/Saipan'), ('America/Porto_Velho', 'America/Porto_Velho'), ('America/Dawson', 'America/Dawson'), ('Asia/Magadan', 'Asia/Magadan'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Asia/Taipei', 'Asia/Taipei'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Europe/Riga', 'Europe/Riga'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Dominica', 'America/Dominica'), ('Africa/Libreville', 'Africa/Libreville'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Atlantic/Azores', 'Atlantic/Azores'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Pacific/Yap', 'Pacific/Yap'), ('America/Nipigon', 'America/Nipigon'), ('Asia/Beirut', 'Asia/Beirut'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Europe/Monaco', 'Europe/Monaco'), ('Europe/Simferopol', 'Europe/Simferopol'), ('America/Vancouver', 'America/Vancouver'), ('America/Indianapolis', 'America/Indianapolis'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Pacific/Midway', 'Pacific/Midway'), ('Asia/Bangkok', 'Asia/Bangkok'), ('PST8PDT', 'PST8PDT'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Australia/Perth', 'Australia/Perth'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Winnipeg', 'America/Winnipeg'), ('Greenwich', 'Greenwich'), ('Asia/Thimbu', 'Asia/Thimbu'), ('America/Menominee', 'America/Menominee'), ('Europe/Athens', 'Europe/Athens'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Africa/Tunis', 'Africa/Tunis'), ('UCT', 'UCT'), ('Etc/GMT0', 'Etc/GMT0'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('America/Antigua', 'America/Antigua'), ('Africa/Juba', 'Africa/Juba'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Africa/Accra', 'Africa/Accra'), ('America/Mexico_City', 'America/Mexico_City'), ('GB', 'GB'), ('Asia/Kabul', 'Asia/Kabul'), ('Australia/Victoria', 'Australia/Victoria'), ('America/El_Salvador', 'America/El_Salvador'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Asia/Tehran', 'Asia/Tehran'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('America/Sitka', 'America/Sitka'), ('America/Marigot', 'America/Marigot'), ('Etc/GMT-9', 'Etc/GMT-9'), ('America/New_York', 'America/New_York'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Montevideo', 'America/Montevideo'), ('Australia/Darwin', 'Australia/Darwin'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Yellowknife', 'America/Yellowknife'), ('America/Iqaluit', 'America/Iqaluit'), ('America/Santiago', 'America/Santiago'), ('Asia/Yangon', 'Asia/Yangon'), ('Turkey', 'Turkey'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Miquelon', 'America/Miquelon'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Europe/Vienna', 'Europe/Vienna'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('America/Toronto', 'America/Toronto'), ('America/Cayman', 'America/Cayman'), ('America/Halifax', 'America/Halifax'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('America/Montserrat', 'America/Montserrat'), ('Europe/Zurich', 'Europe/Zurich'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Africa/Windhoek', 'Africa/Windhoek'), ('America/Inuvik', 'America/Inuvik'), ('EST', 'EST'), ('Europe/Istanbul', 'Europe/Istanbul'), ('America/Ensenada', 'America/Ensenada'), ('Africa/Freetown', 'Africa/Freetown'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Jamaica', 'Jamaica'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('MST', 'MST'), ('America/Creston', 'America/Creston'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('America/Adak', 'America/Adak'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Europe/Oslo', 'Europe/Oslo'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Etc/Zulu', 'Etc/Zulu'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/Regina', 'America/Regina'), ('Iran', 'Iran'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('America/Shiprock', 'America/Shiprock'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Anguilla', 'America/Anguilla'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Denver', 'America/Denver'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Africa/Kampala', 'Africa/Kampala'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('America/Thule', 'America/Thule'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Europe/Jersey', 'Europe/Jersey'), ('Kwajalein', 'Kwajalein'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Indian/Mahe', 'Indian/Mahe'), ('Pacific/Truk', 'Pacific/Truk')], max_length=255),
        ),
    ]