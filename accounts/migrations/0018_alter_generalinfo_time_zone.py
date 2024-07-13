# Generated by Django 5.0.3 on 2024-07-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_generalinfo_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='time_zone',
            field=models.CharField(choices=[('America/Aruba', 'America/Aruba'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Brazil/Acre', 'Brazil/Acre'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Asia/Oral', 'Asia/Oral'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Australia/Brisbane', 'Australia/Brisbane'), ('America/Menominee', 'America/Menominee'), ('America/Merida', 'America/Merida'), ('America/Sitka', 'America/Sitka'), ('Africa/Kampala', 'Africa/Kampala'), ('America/Shiprock', 'America/Shiprock'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/Santiago', 'America/Santiago'), ('Asia/Atyrau', 'Asia/Atyrau'), ('America/New_York', 'America/New_York'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Universal', 'Universal'), ('America/Grenada', 'America/Grenada'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Turkey', 'Turkey'), ('Indian/Reunion', 'Indian/Reunion'), ('America/Tijuana', 'America/Tijuana'), ('America/Winnipeg', 'America/Winnipeg'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Europe/London', 'Europe/London'), ('ROK', 'ROK'), ('Pacific/Johnston', 'Pacific/Johnston'), ('America/Indianapolis', 'America/Indianapolis'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Africa/Accra', 'Africa/Accra'), ('Australia/Perth', 'Australia/Perth'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Europe/Belfast', 'Europe/Belfast'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Africa/Asmera', 'Africa/Asmera'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Europe/Oslo', 'Europe/Oslo'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Iran', 'Iran'), ('America/Nuuk', 'America/Nuuk'), ('Africa/Maseru', 'Africa/Maseru'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('America/Toronto', 'America/Toronto'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Canada/Central', 'Canada/Central'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('America/Metlakatla', 'America/Metlakatla'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('America/Resolute', 'America/Resolute'), ('GB-Eire', 'GB-Eire'), ('Iceland', 'Iceland'), ('America/Rosario', 'America/Rosario'), ('America/St_Thomas', 'America/St_Thomas'), ('America/Phoenix', 'America/Phoenix'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('America/Asuncion', 'America/Asuncion'), ('America/Matamoros', 'America/Matamoros'), ('America/Louisville', 'America/Louisville'), ('Africa/Djibouti', 'Africa/Djibouti'), ('America/Antigua', 'America/Antigua'), ('America/Catamarca', 'America/Catamarca'), ('Etc/GMT-12', 'Etc/GMT-12'), ('US/Samoa', 'US/Samoa'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('US/Alaska', 'US/Alaska'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Chicago', 'America/Chicago'), ('Canada/Yukon', 'Canada/Yukon'), ('Africa/Juba', 'Africa/Juba'), ('America/Cayenne', 'America/Cayenne'), ('Asia/Tehran', 'Asia/Tehran'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Europe/Moscow', 'Europe/Moscow'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Africa/Bangui', 'Africa/Bangui'), ('Africa/Algiers', 'Africa/Algiers'), ('America/Dominica', 'America/Dominica'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Australia/Hobart', 'Australia/Hobart'), ('GMT-0', 'GMT-0'), ('Hongkong', 'Hongkong'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Asia/Macao', 'Asia/Macao'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Europe/Berlin', 'Europe/Berlin'), ('Europe/Busingen', 'Europe/Busingen'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Atka', 'America/Atka'), ('Asia/Saigon', 'Asia/Saigon'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Asia/Tashkent', 'Asia/Tashkent'), ('GB', 'GB'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Europe/Saratov', 'Europe/Saratov'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('America/St_Lucia', 'America/St_Lucia'), ('Europe/Brussels', 'Europe/Brussels'), ('Africa/Douala', 'Africa/Douala'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Nipigon', 'America/Nipigon'), ('Antarctica/Davis', 'Antarctica/Davis'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('America/Montserrat', 'America/Montserrat'), ('America/Swift_Current', 'America/Swift_Current'), ('Asia/Chongqing', 'Asia/Chongqing'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('America/Grand_Turk', 'America/Grand_Turk'), ('GMT0', 'GMT0'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('America/St_Kitts', 'America/St_Kitts'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Pacific/Efate', 'Pacific/Efate'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('America/Guatemala', 'America/Guatemala'), ('Australia/Darwin', 'Australia/Darwin'), ('Europe/Dublin', 'Europe/Dublin'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Pacific/Yap', 'Pacific/Yap'), ('CET', 'CET'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Europe/Riga', 'Europe/Riga'), ('America/Yakutat', 'America/Yakutat'), ('Africa/Cairo', 'Africa/Cairo'), ('US/Central', 'US/Central'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Martinique', 'America/Martinique'), ('Africa/Lagos', 'Africa/Lagos'), ('Africa/Dakar', 'Africa/Dakar'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('America/Curacao', 'America/Curacao'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Pacific/Midway', 'Pacific/Midway'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Asia/Dubai', 'Asia/Dubai'), ('America/Recife', 'America/Recife'), ('America/Havana', 'America/Havana'), ('Africa/Lome', 'Africa/Lome'), ('America/Dawson', 'America/Dawson'), ('CST6CDT', 'CST6CDT'), ('Australia/South', 'Australia/South'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Asia/Anadyr', 'Asia/Anadyr'), ('America/Jamaica', 'America/Jamaica'), ('Europe/Andorra', 'Europe/Andorra'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Asia/Manila', 'Asia/Manila'), ('Europe/Warsaw', 'Europe/Warsaw'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Jamaica', 'Jamaica'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('America/Halifax', 'America/Halifax'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('America/Barbados', 'America/Barbados'), ('UCT', 'UCT'), ('Australia/North', 'Australia/North'), ('America/Jujuy', 'America/Jujuy'), ('Asia/Colombo', 'Asia/Colombo'), ('Indian/Christmas', 'Indian/Christmas'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('EET', 'EET'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Eirunepe', 'America/Eirunepe'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Zulu', 'Zulu'), ('America/Monterrey', 'America/Monterrey'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Fortaleza', 'America/Fortaleza'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Pacific/Truk', 'Pacific/Truk'), ('Africa/Malabo', 'Africa/Malabo'), ('Africa/Harare', 'Africa/Harare'), ('Asia/Harbin', 'Asia/Harbin'), ('Asia/Chungking', 'Asia/Chungking'), ('America/El_Salvador', 'America/El_Salvador'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Canada/Mountain', 'Canada/Mountain'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Adak', 'America/Adak'), ('Asia/Famagusta', 'Asia/Famagusta'), ('America/Iqaluit', 'America/Iqaluit'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Asia/Karachi', 'Asia/Karachi'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Pacific/Easter', 'Pacific/Easter'), ('Africa/Conakry', 'Africa/Conakry'), ('GMT', 'GMT'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Etc/UCT', 'Etc/UCT'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Europe/Monaco', 'Europe/Monaco'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Canada/Pacific', 'Canada/Pacific'), ('Asia/Jakarta', 'Asia/Jakarta'), ('US/Arizona', 'US/Arizona'), ('Asia/Nicosia', 'Asia/Nicosia'), ('America/Bogota', 'America/Bogota'), ('Libya', 'Libya'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Pacific/Guam', 'Pacific/Guam'), ('Australia/Canberra', 'Australia/Canberra'), ('America/Cordoba', 'America/Cordoba'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Asia/Makassar', 'Asia/Makassar'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Europe/Samara', 'Europe/Samara'), ('Portugal', 'Portugal'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Navajo', 'Navajo'), ('US/Michigan', 'US/Michigan'), ('America/Noronha', 'America/Noronha'), ('Africa/Bamako', 'Africa/Bamako'), ('EST', 'EST'), ('Pacific/Palau', 'Pacific/Palau'), ('America/Atikokan', 'America/Atikokan'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Asia/Gaza', 'Asia/Gaza'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/St_Johns', 'America/St_Johns'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Africa/Niamey', 'Africa/Niamey'), ('Asia/Chita', 'Asia/Chita'), ('America/Cayman', 'America/Cayman'), ('Europe/Nicosia', 'Europe/Nicosia'), ('America/Cuiaba', 'America/Cuiaba'), ('MET', 'MET'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Chile/Continental', 'Chile/Continental'), ('Europe/Sofia', 'Europe/Sofia'), ('America/Managua', 'America/Managua'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Etc/GMT-3', 'Etc/GMT-3'), ('America/Godthab', 'America/Godthab'), ('America/Lima', 'America/Lima'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('America/Maceio', 'America/Maceio'), ('Europe/Vienna', 'Europe/Vienna'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Australia/ACT', 'Australia/ACT'), ('NZ-CHAT', 'NZ-CHAT'), ('Europe/Chisinau', 'Europe/Chisinau'), ('America/Inuvik', 'America/Inuvik'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Asia/Baku', 'Asia/Baku'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Asia/Beirut', 'Asia/Beirut'), ('Asia/Hebron', 'Asia/Hebron'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Indian/Mauritius', 'Indian/Mauritius'), ('PRC', 'PRC'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Israel', 'Israel'), ('Pacific/Majuro', 'Pacific/Majuro'), ('America/Mendoza', 'America/Mendoza'), ('Asia/Dacca', 'Asia/Dacca'), ('America/Hermosillo', 'America/Hermosillo'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('America/Montevideo', 'America/Montevideo'), ('Australia/Eucla', 'Australia/Eucla'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Africa/Gaborone', 'Africa/Gaborone'), ('US/East-Indiana', 'US/East-Indiana'), ('UTC', 'UTC'), ('Australia/Currie', 'Australia/Currie'), ('America/Santarem', 'America/Santarem'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('America/Guadeloupe', 'America/Guadeloupe'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Brazil/West', 'Brazil/West'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Etc/Zulu', 'Etc/Zulu'), ('US/Pacific', 'US/Pacific'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Asia/Omsk', 'Asia/Omsk'), ('America/Anchorage', 'America/Anchorage'), ('America/Vancouver', 'America/Vancouver'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Denver', 'America/Denver'), ('America/Araguaina', 'America/Araguaina'), ('America/Belem', 'America/Belem'), ('Asia/Magadan', 'Asia/Magadan'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('EST5EDT', 'EST5EDT'), ('Eire', 'Eire'), ('Africa/Kigali', 'Africa/Kigali'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Singapore', 'Singapore'), ('Mexico/General', 'Mexico/General'), ('Greenwich', 'Greenwich'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Asia/Almaty', 'Asia/Almaty'), ('Europe/Malta', 'Europe/Malta'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Nassau', 'America/Nassau'), ('Asia/Baghdad', 'Asia/Baghdad'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Juneau', 'America/Juneau'), ('Etc/Universal', 'Etc/Universal'), ('America/Nome', 'America/Nome'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Asia/Dili', 'Asia/Dili'), ('Pacific/Gambier', 'Pacific/Gambier'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Europe/Skopje', 'Europe/Skopje'), ('Asia/Muscat', 'Asia/Muscat'), ('America/Mazatlan', 'America/Mazatlan'), ('HST', 'HST'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('US/Hawaii', 'US/Hawaii'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/Manaus', 'America/Manaus'), ('Europe/Paris', 'Europe/Paris'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('America/Virgin', 'America/Virgin'), ('America/Mexico_City', 'America/Mexico_City'), ('America/St_Vincent', 'America/St_Vincent'), ('America/Marigot', 'America/Marigot'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Etc/GMT+4', 'Etc/GMT+4'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Pacific/Niue', 'Pacific/Niue'), ('America/Anguilla', 'America/Anguilla'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Indian/Maldives', 'Indian/Maldives'), ('Africa/Libreville', 'Africa/Libreville'), ('Africa/Tunis', 'Africa/Tunis'), ('Asia/Yangon', 'Asia/Yangon'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/Kralendijk', 'America/Kralendijk'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Europe/Zurich', 'Europe/Zurich'), ('America/Montreal', 'America/Montreal'), ('PST8PDT', 'PST8PDT'), ('W-SU', 'W-SU'), ('Africa/Freetown', 'Africa/Freetown'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Asia/Qostanay', 'Asia/Qostanay'), ('America/Boise', 'America/Boise'), ('Asia/Seoul', 'Asia/Seoul'), ('Europe/Jersey', 'Europe/Jersey'), ('GMT+0', 'GMT+0'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Etc/GMT0', 'Etc/GMT0'), ('Asia/Calcutta', 'Asia/Calcutta'), ('America/Ensenada', 'America/Ensenada'), ('Japan', 'Japan'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/Tortola', 'America/Tortola'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Europe/Minsk', 'Europe/Minsk'), ('Europe/Vilnius', 'Europe/Vilnius'), ('America/Whitehorse', 'America/Whitehorse'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Australia/NSW', 'Australia/NSW'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Etc/GMT-13', 'Etc/GMT-13'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Etc/GMT+2', 'Etc/GMT+2'), ('WET', 'WET'), ('Europe/Prague', 'Europe/Prague'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('America/La_Paz', 'America/La_Paz'), ('MST7MDT', 'MST7MDT'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Asia/Kuching', 'Asia/Kuching'), ('Etc/GMT-11', 'Etc/GMT-11'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Guyana', 'America/Guyana'), ('America/Regina', 'America/Regina'), ('America/Rainy_River', 'America/Rainy_River'), ('America/Edmonton', 'America/Edmonton'), ('Asia/Brunei', 'Asia/Brunei'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Europe/Kirov', 'Europe/Kirov'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Asia/Taipei', 'Asia/Taipei'), ('Etc/GMT+6', 'Etc/GMT+6'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Australia/Queensland', 'Australia/Queensland'), ('Africa/Banjul', 'Africa/Banjul'), ('US/Mountain', 'US/Mountain'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Australia/Adelaide', 'Australia/Adelaide'), ('America/Knox_IN', 'America/Knox_IN'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('America/Miquelon', 'America/Miquelon'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Africa/Maputo', 'Africa/Maputo'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Asia/Hovd', 'Asia/Hovd'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Bahia', 'America/Bahia'), ('America/Creston', 'America/Creston'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Australia/Victoria', 'Australia/Victoria'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Pacific/Apia', 'Pacific/Apia'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Caracas', 'America/Caracas'), ('Europe/Rome', 'Europe/Rome'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Europe/Tirane', 'Europe/Tirane'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Australia/Sydney', 'Australia/Sydney'), ('Asia/Singapore', 'Asia/Singapore'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('MST', 'MST'), ('America/Moncton', 'America/Moncton'), ('NZ', 'NZ'), ('Europe/Vatican', 'Europe/Vatican'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Poland', 'Poland'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/Panama', 'America/Panama'), ('America/Chihuahua', 'America/Chihuahua'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Europe/Kiev', 'Europe/Kiev'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Europe/Madrid', 'Europe/Madrid'), ('Canada/Eastern', 'Canada/Eastern'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Etc/GMT+7', 'Etc/GMT+7'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Etc/GMT+11', 'Etc/GMT+11'), ('US/Aleutian', 'US/Aleutian'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Australia/LHI', 'Australia/LHI'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('ROC', 'ROC'), ('America/Yellowknife', 'America/Yellowknife'), ('Asia/Macau', 'Asia/Macau'), ('Cuba', 'Cuba'), ('Egypt', 'Egypt'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Etc/GMT', 'Etc/GMT'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Pacific/Wake', 'Pacific/Wake'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Brazil/East', 'Brazil/East'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Indian/Mahe', 'Indian/Mahe'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Kwajalein', 'Kwajalein'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('America/Cancun', 'America/Cancun'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Asia/Damascus', 'Asia/Damascus'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/Thule', 'America/Thule'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Indian/Comoro', 'Indian/Comoro'), ('Asia/Aden', 'Asia/Aden'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Asia/Amman', 'Asia/Amman'), ('Etc/GMT-1', 'Etc/GMT-1'), ('US/Eastern', 'US/Eastern'), ('Indian/Cocos', 'Indian/Cocos'), ('Asia/Kabul', 'Asia/Kabul'), ('Etc/UTC', 'Etc/UTC'), ('America/Belize', 'America/Belize'), ('America/Detroit', 'America/Detroit'), ('Etc/Greenwich', 'Etc/Greenwich'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Australia/West', 'Australia/West'), ('Africa/Asmara', 'Africa/Asmara'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Europe/Athens', 'Europe/Athens'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Africa/Blantyre', 'Africa/Blantyre')], max_length=255),
        ),
    ]