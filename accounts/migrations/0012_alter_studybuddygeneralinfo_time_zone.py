# Generated by Django 5.0.3 on 2024-07-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_studybuddygeneralinfo_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studybuddygeneralinfo',
            name='time_zone',
            field=models.CharField(choices=[('Europe/Riga', 'Europe/Riga'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Asia/Amman', 'Asia/Amman'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Halifax', 'America/Halifax'), ('Asia/Baku', 'Asia/Baku'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Europe/Oslo', 'Europe/Oslo'), ('Europe/Jersey', 'Europe/Jersey'), ('America/Aruba', 'America/Aruba'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('America/Knox_IN', 'America/Knox_IN'), ('Europe/Dublin', 'Europe/Dublin'), ('Kwajalein', 'Kwajalein'), ('America/St_Lucia', 'America/St_Lucia'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('America/Adak', 'America/Adak'), ('Turkey', 'Turkey'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Martinique', 'America/Martinique'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Indian/Maldives', 'Indian/Maldives'), ('Europe/Busingen', 'Europe/Busingen'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Australia/Brisbane', 'Australia/Brisbane'), ('America/St_Johns', 'America/St_Johns'), ('America/Nome', 'America/Nome'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Asia/Oral', 'Asia/Oral'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('America/Barbados', 'America/Barbados'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Asia/Dhaka', 'Asia/Dhaka'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Pacific/Wake', 'Pacific/Wake'), ('Australia/Hobart', 'Australia/Hobart'), ('Africa/Kampala', 'Africa/Kampala'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Africa/Tripoli', 'Africa/Tripoli'), ('America/Nipigon', 'America/Nipigon'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('US/Pacific', 'US/Pacific'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Asia/Hovd', 'Asia/Hovd'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Jamaica', 'Jamaica'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Africa/Juba', 'Africa/Juba'), ('America/Regina', 'America/Regina'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Zulu', 'Zulu'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/St_Thomas', 'America/St_Thomas'), ('Europe/Athens', 'Europe/Athens'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Africa/Tunis', 'Africa/Tunis'), ('Asia/Muscat', 'Asia/Muscat'), ('Europe/London', 'Europe/London'), ('Europe/Samara', 'Europe/Samara'), ('America/Havana', 'America/Havana'), ('Europe/Minsk', 'Europe/Minsk'), ('America/Denver', 'America/Denver'), ('America/Monterrey', 'America/Monterrey'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Asia/Dubai', 'Asia/Dubai'), ('Europe/Tirane', 'Europe/Tirane'), ('America/Manaus', 'America/Manaus'), ('America/Resolute', 'America/Resolute'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('America/Montserrat', 'America/Montserrat'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('America/Recife', 'America/Recife'), ('US/Samoa', 'US/Samoa'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Pacific/Easter', 'Pacific/Easter'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Asia/Aqtau', 'Asia/Aqtau'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Europe/Bratislava', 'Europe/Bratislava'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Australia/Sydney', 'Australia/Sydney'), ('America/Boise', 'America/Boise'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Iqaluit', 'America/Iqaluit'), ('Etc/GMT-3', 'Etc/GMT-3'), ('America/El_Salvador', 'America/El_Salvador'), ('Australia/ACT', 'Australia/ACT'), ('Europe/Bucharest', 'Europe/Bucharest'), ('NZ', 'NZ'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Asia/Khandyga', 'Asia/Khandyga'), ('America/Edmonton', 'America/Edmonton'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Africa/Cairo', 'Africa/Cairo'), ('Africa/Douala', 'Africa/Douala'), ('Portugal', 'Portugal'), ('America/Belem', 'America/Belem'), ('Australia/Perth', 'Australia/Perth'), ('GMT0', 'GMT0'), ('America/Indianapolis', 'America/Indianapolis'), ('America/Winnipeg', 'America/Winnipeg'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Cayenne', 'America/Cayenne'), ('Etc/GMT+3', 'Etc/GMT+3'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Nuuk', 'America/Nuuk'), ('Pacific/Apia', 'Pacific/Apia'), ('Asia/Tashkent', 'Asia/Tashkent'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Etc/GMT0', 'Etc/GMT0'), ('Africa/Luanda', 'Africa/Luanda'), ('MST7MDT', 'MST7MDT'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Canada/Pacific', 'Canada/Pacific'), ('Africa/Libreville', 'Africa/Libreville'), ('US/Mountain', 'US/Mountain'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/Thule', 'America/Thule'), ('Eire', 'Eire'), ('Asia/Dacca', 'Asia/Dacca'), ('America/St_Kitts', 'America/St_Kitts'), ('America/Grand_Turk', 'America/Grand_Turk'), ('America/Yakutat', 'America/Yakutat'), ('Antarctica/Troll', 'Antarctica/Troll'), ('GB-Eire', 'GB-Eire'), ('America/Ensenada', 'America/Ensenada'), ('Africa/Kigali', 'Africa/Kigali'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Virgin', 'America/Virgin'), ('America/Marigot', 'America/Marigot'), ('Australia/South', 'Australia/South'), ('US/Michigan', 'US/Michigan'), ('Asia/Kuching', 'Asia/Kuching'), ('America/Vancouver', 'America/Vancouver'), ('Asia/Macau', 'Asia/Macau'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Iran', 'Iran'), ('America/Ojinaga', 'America/Ojinaga'), ('Africa/Freetown', 'Africa/Freetown'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Asia/Brunei', 'Asia/Brunei'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('US/Hawaii', 'US/Hawaii'), ('Europe/Kyiv', 'Europe/Kyiv'), ('America/Mendoza', 'America/Mendoza'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Shanghai', 'Asia/Shanghai'), ('GMT-0', 'GMT-0'), ('Europe/Paris', 'Europe/Paris'), ('Asia/Chita', 'Asia/Chita'), ('Europe/Andorra', 'Europe/Andorra'), ('GMT', 'GMT'), ('America/Chicago', 'America/Chicago'), ('America/Grenada', 'America/Grenada'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Australia/LHI', 'Australia/LHI'), ('America/Fortaleza', 'America/Fortaleza'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Pacific/Majuro', 'Pacific/Majuro'), ('America/Detroit', 'America/Detroit'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Chile/Continental', 'Chile/Continental'), ('America/Merida', 'America/Merida'), ('America/Santarem', 'America/Santarem'), ('Asia/Famagusta', 'Asia/Famagusta'), ('America/Paramaribo', 'America/Paramaribo'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Asia/Samarkand', 'Asia/Samarkand'), ('America/Curacao', 'America/Curacao'), ('CST6CDT', 'CST6CDT'), ('Africa/Niamey', 'Africa/Niamey'), ('America/Mazatlan', 'America/Mazatlan'), ('America/La_Paz', 'America/La_Paz'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Europe/Skopje', 'Europe/Skopje'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('America/Dawson', 'America/Dawson'), ('Pacific/Efate', 'Pacific/Efate'), ('ROK', 'ROK'), ('America/Tijuana', 'America/Tijuana'), ('US/East-Indiana', 'US/East-Indiana'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Montreal', 'America/Montreal'), ('Mexico/General', 'Mexico/General'), ('Asia/Saigon', 'Asia/Saigon'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Europe/Saratov', 'Europe/Saratov'), ('America/Toronto', 'America/Toronto'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Africa/Asmera', 'Africa/Asmera'), ('NZ-CHAT', 'NZ-CHAT'), ('America/Creston', 'America/Creston'), ('Europe/Sofia', 'Europe/Sofia'), ('Asia/Tokyo', 'Asia/Tokyo'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Juneau', 'America/Juneau'), ('Europe/Kiev', 'Europe/Kiev'), ('America/Dominica', 'America/Dominica'), ('UTC', 'UTC'), ('Europe/Lisbon', 'Europe/Lisbon'), ('America/Cordoba', 'America/Cordoba'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Asia/Magadan', 'Asia/Magadan'), ('America/Miquelon', 'America/Miquelon'), ('America/Managua', 'America/Managua'), ('Canada/Central', 'Canada/Central'), ('Etc/GMT-2', 'Etc/GMT-2'), ('America/Louisville', 'America/Louisville'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Iceland', 'Iceland'), ('GMT+0', 'GMT+0'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('America/St_Vincent', 'America/St_Vincent'), ('Etc/Zulu', 'Etc/Zulu'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Pacific/Truk', 'Pacific/Truk'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Asia/Manila', 'Asia/Manila'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('US/Aleutian', 'US/Aleutian'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Etc/GMT+8', 'Etc/GMT+8'), ('MET', 'MET'), ('Europe/Vatican', 'Europe/Vatican'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Pacific/Noumea', 'Pacific/Noumea'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('America/Kralendijk', 'America/Kralendijk'), ('Australia/Darwin', 'Australia/Darwin'), ('Etc/GMT+10', 'Etc/GMT+10'), ('WET', 'WET'), ('Asia/Harbin', 'Asia/Harbin'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Etc/GMT-11', 'Etc/GMT-11'), ('America/Atka', 'America/Atka'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Africa/Malabo', 'Africa/Malabo'), ('US/Arizona', 'US/Arizona'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Asia/Hebron', 'Asia/Hebron'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Atikokan', 'America/Atikokan'), ('Europe/Guernsey', 'Europe/Guernsey'), ('America/Belize', 'America/Belize'), ('Canada/Yukon', 'Canada/Yukon'), ('America/Shiprock', 'America/Shiprock'), ('America/Menominee', 'America/Menominee'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Indian/Reunion', 'Indian/Reunion'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Pacific/Palau', 'Pacific/Palau'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('ROC', 'ROC'), ('Europe/Berlin', 'Europe/Berlin'), ('Africa/Lome', 'Africa/Lome'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Canada/Mountain', 'Canada/Mountain'), ('Asia/Kashgar', 'Asia/Kashgar'), ('America/Nassau', 'America/Nassau'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Europe/Vienna', 'Europe/Vienna'), ('Etc/GMT+7', 'Etc/GMT+7'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Asia/Kabul', 'Asia/Kabul'), ('Africa/Bangui', 'Africa/Bangui'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Indian/Christmas', 'Indian/Christmas'), ('Etc/GMT-12', 'Etc/GMT-12'), ('W-SU', 'W-SU'), ('Pacific/Niue', 'Pacific/Niue'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('America/Yellowknife', 'America/Yellowknife'), ('America/Caracas', 'America/Caracas'), ('Egypt', 'Egypt'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Etc/Universal', 'Etc/Universal'), ('Australia/Currie', 'Australia/Currie'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Africa/Bissau', 'Africa/Bissau'), ('Europe/Brussels', 'Europe/Brussels'), ('Africa/Lagos', 'Africa/Lagos'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Africa/Accra', 'Africa/Accra'), ('Brazil/West', 'Brazil/West'), ('America/Moncton', 'America/Moncton'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('PST8PDT', 'PST8PDT'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Asia/Dili', 'Asia/Dili'), ('US/Alaska', 'US/Alaska'), ('America/Guyana', 'America/Guyana'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Asia/Yangon', 'Asia/Yangon'), ('US/Central', 'US/Central'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/Cancun', 'America/Cancun'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Canada/Eastern', 'Canada/Eastern'), ('PRC', 'PRC'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Chungking', 'Asia/Chungking'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/Metlakatla', 'America/Metlakatla'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Maceio', 'America/Maceio'), ('America/Santiago', 'America/Santiago'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Africa/Harare', 'Africa/Harare'), ('EET', 'EET'), ('HST', 'HST'), ('Hongkong', 'Hongkong'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Etc/UCT', 'Etc/UCT'), ('Atlantic/Canary', 'Atlantic/Canary'), ('America/Noronha', 'America/Noronha'), ('Japan', 'Japan'), ('Australia/Eucla', 'Australia/Eucla'), ('America/Bogota', 'America/Bogota'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Pacific/Guam', 'Pacific/Guam'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Etc/GMT', 'Etc/GMT'), ('Europe/Tallinn', 'Europe/Tallinn'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Brazil/Acre', 'Brazil/Acre'), ('Asia/Tehran', 'Asia/Tehran'), ('MST', 'MST'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Indian/Mahe', 'Indian/Mahe'), ('Atlantic/Azores', 'Atlantic/Azores'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Africa/Maseru', 'Africa/Maseru'), ('America/New_York', 'America/New_York'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('America/Catamarca', 'America/Catamarca'), ('Singapore', 'Singapore'), ('Australia/West', 'Australia/West'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Cuba', 'Cuba'), ('Pacific/Yap', 'Pacific/Yap'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Greenwich', 'Greenwich'), ('America/Araguaina', 'America/Araguaina'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Asia/Almaty', 'Asia/Almaty'), ('Australia/Queensland', 'Australia/Queensland'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Europe/Malta', 'Europe/Malta'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Asia/Macao', 'Asia/Macao'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Etc/UTC', 'Etc/UTC'), ('Europe/Rome', 'Europe/Rome'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('EST', 'EST'), ('America/Jujuy', 'America/Jujuy'), ('Asia/Baghdad', 'Asia/Baghdad'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Rosario', 'America/Rosario'), ('America/Antigua', 'America/Antigua'), ('Indian/Cocos', 'Indian/Cocos'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Pacific/Auckland', 'Pacific/Auckland'), ('UCT', 'UCT'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Lima', 'America/Lima'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Europe/Monaco', 'Europe/Monaco'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Africa/Algiers', 'Africa/Algiers'), ('Brazil/East', 'Brazil/East'), ('Asia/Singapore', 'Asia/Singapore'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Navajo', 'Navajo'), ('Europe/Volgograd', 'Europe/Volgograd'), ('America/Guatemala', 'America/Guatemala'), ('CET', 'CET'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Aden', 'Asia/Aden'), ('Africa/Maputo', 'Africa/Maputo'), ('Africa/Bamako', 'Africa/Bamako'), ('GB', 'GB'), ('America/Eirunepe', 'America/Eirunepe'), ('America/Panama', 'America/Panama'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('America/Montevideo', 'America/Montevideo'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('America/Cuiaba', 'America/Cuiaba'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Asia/Damascus', 'Asia/Damascus'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Hermosillo', 'America/Hermosillo'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Universal', 'Universal'), ('Australia/Canberra', 'Australia/Canberra'), ('Australia/NSW', 'Australia/NSW'), ('Pacific/Midway', 'Pacific/Midway'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Africa/Asmara', 'Africa/Asmara'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Poland', 'Poland'), ('Africa/Nairobi', 'Africa/Nairobi'), ('America/Jamaica', 'America/Jamaica'), ('America/Tortola', 'America/Tortola'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Asia/Taipei', 'Asia/Taipei'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Asia/Colombo', 'Asia/Colombo'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Etc/GMT+11', 'Etc/GMT+11'), ('US/Eastern', 'US/Eastern'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Asia/Gaza', 'Asia/Gaza'), ('Asia/Karachi', 'Asia/Karachi'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Libya', 'Libya'), ('America/Matamoros', 'America/Matamoros'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Asia/Makassar', 'Asia/Makassar'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Europe/Istanbul', 'Europe/Istanbul'), ('America/Godthab', 'America/Godthab'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Asuncion', 'America/Asuncion'), ('America/Phoenix', 'America/Phoenix'), ('Europe/Zurich', 'Europe/Zurich'), ('Indian/Mayotte', 'Indian/Mayotte'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Anchorage', 'America/Anchorage'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Guayaquil', 'America/Guayaquil'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Europe/Madrid', 'Europe/Madrid'), ('Europe/Prague', 'Europe/Prague'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('America/Swift_Current', 'America/Swift_Current'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Africa/Conakry', 'Africa/Conakry'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Mexico_City', 'America/Mexico_City'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Asia/Beirut', 'Asia/Beirut'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Bahia', 'America/Bahia'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Indian/Comoro', 'Indian/Comoro'), ('America/Rainy_River', 'America/Rainy_River'), ('Europe/Kirov', 'Europe/Kirov'), ('Asia/Seoul', 'Asia/Seoul'), ('Asia/Omsk', 'Asia/Omsk'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Israel', 'Israel'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('EST5EDT', 'EST5EDT'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('America/Sitka', 'America/Sitka'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Australia/Victoria', 'Australia/Victoria'), ('Europe/Belfast', 'Europe/Belfast'), ('America/Cayman', 'America/Cayman'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('America/Campo_Grande', 'America/Campo_Grande'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Inuvik', 'America/Inuvik'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Australia/North', 'Australia/North'), ('America/Anguilla', 'America/Anguilla'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk')], max_length=255),
        ),
    ]