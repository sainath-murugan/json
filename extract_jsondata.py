import json
import requests

request = requests.get("http://www.floatrates.com/daily/inr.json")
request_in_text = request.text

code = ("""usd: U.S. Dollar
eur: Euro
gbp: U.K. Pound Sterling
aud: Australian Dollar
cad: Canadian Dollar
jpy: Japanese Yen
chf: Swiss Franc
mmk: Myanma Kyat
lkr: Sri Lanka Rupee
clp: Chilean Peso
sek: Swedish Krona
php: Philippine Peso
mro: Mauritanian Ouguiya
lbp: Lebanese Pound
gmd: Gambian dalasi
bif: Burundian franc
sll: Sierra Leonean leone
scr: Seychelles rupee
dkk: Danish Krone
aed: U.A.E Dirham
twd: New Taiwan Dollar 
jod: Jordanian Dinar
gel: Georgian lari
bsd: Bahamian Dollar
gnf: Guinean franc
rwf: Rwandan franc
mzn: Mozambican metical
tzs: Tanzanian shilling
cny: Chinese Yuan
kwd: Kuwaiti Dinar
huf: Hungarian Forint
ngn: Nigerian Naira
amd: Armenia Dram
uyu: Uruguayan Peso
gyd: Guyanese dollar
syp: Syrian pound
top: Tongan paʻanga
mnt: Mongolian togrog
nzd: New Zealand Dollar
hrk: Croatian Kuna
byn: Belarussian Ruble
mdl: Moldova Lei
nio: Nicaraguan Córdoba
nad: Namibian dollar
lak: Lao kip
cup: Cuban peso
sar: Saudi Riyal
hkd: Hong Kong Dollar
qar: Qatari Rial
uzs: Uzbekistan Sum
pab: Panamanian Balboa
xcd: East Caribbean Dollar
aoa: Angolan kwanza
khr: Cambodian riel
zar: South African Rand
mxn: Mexican Peso
lyd: Libyan Dinar
iqd: Iraqi dinar
svc: Salvadoran colon
awg: Aruban florin
hnl: Honduran Lempira
npr: Nepalese Rupee
czk: Czech Koruna
thb: Thai Baht
xof: West African CFA Franc
egp: Egyptian Pound
rsd: Serbian Dinar
stn: São Tomé and Príncipe Dobra
djf: Djiboutian franc
cdf: Congolese franc
lsl: Lesotho loti
sos: Somali shilling
krw: South Korean Won
bgn: Bulgarian Lev
pgk: Papua New Guinean kina
azn: Azerbaijan Manat
pyg: Paraguayan Guaraní
fjd: Fiji Dollar
sdg: Sudanese pound
mru: Mauritanian ouguiya
wst: Samoan tala
mur: Mauritian Rupee
isk: Icelandic Krona
pkr: Pakistani Rupee
kgs: Kyrgyzstan Som
crc: Costa Rican Colón
lrd: Liberian dollar
ang: Neth. Antillean Guilder
dop: Dominican Peso
bam: Bosnia and Herzegovina convertible mark
dzd: Algerian Dinar
pln: Polish Zloty
brl: Brazilian Real
gip: Gibraltar pound
tmt: New Turkmenistan Manat
mga: Malagasy ariary
ttd: Trinidad Tobago Dollar
zmw: Zambian kwacha
yer: Yemeni rial
bnd: Brunei Dollar
sgd: Singapore Dollar
ils: Israeli New Sheqel
tnd: Tunisian Dinar
irr: Iranian rial
ves: Venezuelan Bolivar
cve: Cape Verde escudo
all: Albanian lek
mvr: Maldivian rufiyaa
cop: Colombian Peso
xaf: Central African CFA Franc
omr: Omani Rial
ghs: Ghanaian Cedi
mkd: Macedonian denar
xpf: CFP Franc
kmf: 	Comoro franc
szl: Swazi lilangeni
kes: Kenyan shilling
bbd: Barbadian Dollar
vnd: Vietnamese Dong
mad: Moroccan Dirham
ars: Argentine Peso
bzd: Belize dollar
ssp: South Sudanese pound
ern: Eritrean nakfa
ugx: Ugandan shilling
myr: Malaysian Ringgit
ron: Romanian New Leu
pen: Peruvian Nuevo Sol
kzt: Kazakhstani Tenge
bob: Bolivian Boliviano
jmd: Jamaican Dollar
htg: Haitian gourde
mop: Macanese pataca
vuv: Vanuatu vatu
nok: Norwegian Krone
try: Turkish Lira
bdt: Bangladeshi taka
tjs: Tajikistan Ruble
afn: Afghan afghani
srd: Surinamese dollar
mwk: Malawian kwacha
gtq: Guatemalan Quetzal
bwp: Botswana Pula
rub: Russian Rouble
idr: Indonesian Rupiah
bhd: Bahrain Dinar
uah: Ukrainian Hryvnia
etb: Ethiopian birr
sbd: Solomon Islands dollar\n\n\n""")


class JsonCurrency:

    def __init__(self):
        self.data = json.loads(request_in_text)

    def specific_detail(self, country_code):

        for key, value in self.data[country_code.lower()].items():
            print(f"{key}: {value}")

    def currency_detail(self, country_code):

        print(f"the equivalent {country_code} for one indian rupee is "
              f"{round(self.data[country_code.lower()]['rate'], 2)} {country_code}")
        print(f"the equivalent indian rupee for one {country_code} is "
              f"{round(self.data[country_code.lower()]['inverseRate'],2)} rupee")


s1 = JsonCurrency()
choice = int(input("1. TO KNOW DETAIL OF SPECIFIC COUNTRY\n"
                   "2. TO KNOW THE DETAIL OF SPECIFIC COUNTRY CURRENCY\n"))
if choice == 1:
    print(code)
    enter_value = input("enter a country code of any country from the above list")
    s1.specific_detail(enter_value)

if choice == 2:
    print(code)
    enter_value = input("enter a code of any country from the above list to know the currency detail")
    s1.currency_detail(enter_value)
