"""Approved message library (six languages) and how a message is assembled.
The AI never writes text: every message is built only from these pieces.
Tamil, Kannada and Marathi wording was reviewed and approved by native speakers."""

LANGS = ['English', 'Hinglish', 'Hindi', 'Marathi', 'Tamil', 'Kannada']

GREET = {'English': 'Dear Valued Merchant,',
 'Hinglish': 'Dear Valued Merchant,',
 'Hindi': 'आदरणीय व्यापारी,',
 'Marathi': 'आदरणीय व्यापारी,',
 'Tamil': 'மதிப்பிற்குரிய வணிகரே,',
 'Kannada': 'ಗೌರವಾನ್ವಿತ ವ್ಯಾಪಾರಿಗಳೇ,'}

HEAD = {'soft': {'English': 'Your Razorpay application needs one update from you.',
          'Hinglish': 'Aapki Razorpay application mein aapki taraf se ek update chahiye.',
          'Hindi': 'आपके Razorpay आवेदन में आपकी ओर से एक अपडेट चाहिए।',
          'Marathi': 'तुमच्या Razorpay अर्जासाठी तुमच्याकडून एक अपडेट हवा आहे.',
          'Tamil': 'உங்கள் Razorpay விண்ணப்பத்திற்கு உங்களிடமிருந்து ஒரு புதுப்பிப்பு தேவை.',
          'Kannada': 'ನಿಮ್ಮ Razorpay ಅರ್ಜಿಗೆ ನಿಮ್ಮಿಂದ ಒಂದು ಅಪ್\u200cಡೇಟ್ ಬೇಕಾಗಿದೆ.'},
 'reminder': {'English': 'Your Razorpay application is still waiting for you.',
              'Hinglish': 'Aapki Razorpay application abhi bhi aapka intezaar kar rahi hai.',
              'Hindi': 'आपका Razorpay आवेदन अभी भी आपका इंतज़ार कर रहा है।',
              'Marathi': 'तुमचा Razorpay अर्ज अजूनही तुमची वाट पाहत आहे.',
              'Tamil': 'உங்கள் Razorpay விண்ணப்பம் இன்னும் உங்களுக்காகக் காத்திருக்கிறது.',
              'Kannada': 'ನಿಮ್ಮ Razorpay ಅರ್ಜಿ ಇನ್ನೂ ನಿಮಗಾಗಿ ಕಾಯುತ್ತಿದೆ.'},
 'gentle': {'English': 'We are here whenever you are ready to finish your Razorpay application.',
            'Hinglish': 'Jab aap taiyaar hon, hum aapki Razorpay application poori karne mein madad karenge.',
            'Hindi': 'जब भी आप अपना Razorpay आवेदन पूरा करना चाहें, हम मदद के लिए यहाँ हैं।',
            'Marathi': 'तुम्ही जेव्हा तुमचा Razorpay अर्ज पूर्ण करायला तयार असाल, तेव्हा आम्ही मदतीसाठी इथे आहोत.',
            'Tamil': 'நீங்கள் தயாரானதும் உங்கள் Razorpay விண்ணப்பத்தை முடிக்க நாங்கள் உதவுவோம்.',
            'Kannada': 'ನಿಮ್ಮ Razorpay ಅರ್ಜಿಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ನೀವು ಸಿದ್ಧರಾದಾಗ, ನಾವು ಸಹಾಯಕ್ಕೆ ಇಲ್ಲಿದ್ದೇವೆ.'},
 'r13soft': {'English': 'Your Razorpay application is ready to continue.',
             'Hinglish': 'Aapki Razorpay application aage badhne ke liye taiyaar hai.',
             'Hindi': 'आपका Razorpay आवेदन आगे बढ़ने के लिए तैयार है।',
             'Marathi': 'तुमचा Razorpay अर्ज पुढे सुरू ठेवण्यासाठी तयार आहे.',
             'Tamil': 'உங்கள் Razorpay விண்ணப்பம் தொடர தயாராக உள்ளது.',
             'Kannada': 'ನಿಮ್ಮ Razorpay ಅರ್ಜಿ ಮುಂದುವರಿಸಲು ಸಿದ್ಧವಾಗಿದೆ.'}}

STEP_LINE = {'English': 'It is currently at the {step} step.',
 'Hinglish': 'Abhi yeh {step} step par hai.',
 'Hindi': 'अभी यह {step} चरण पर है।',
 'Marathi': 'सध्या हा {step} टप्प्यावर आहे.',
 'Tamil': 'தற்போது இது {step} படியில் உள்ளது.',
 'Kannada': 'ಸದ್ಯ ಇದು {step} ಹಂತದಲ್ಲಿದೆ.'}

STEPWORD = {'English': 'step', 'Hinglish': 'step', 'Hindi': 'चरण', 'Marathi': 'टप्पा', 'Tamil': 'படி', 'Kannada': 'ಹಂತ'}

EMPATHY = {'English': 'We are sorry this has taken some effort.',
 'Hinglish': 'Hume khed hai ki ismein aapko itni mehnat lagi.',
 'Hindi': 'हमें खेद है कि इसमें आपको काफ़ी मेहनत करनी पड़ी।',
 'Marathi': 'यासाठी तुम्हाला खूप मेहनत करावी लागली, याबद्दल आम्हाला खेद वाटतो.',
 'Tamil': 'இதற்கு நீங்கள் நிறைய முயற்சி செய்ததற்கு வருந்துகிறோம்.',
 'Kannada': 'ಇದಕ್ಕಾಗಿ ನೀವು ತುಂಬಾ ಶ್ರಮಪಡಬೇಕಾಯಿತು, ಅದಕ್ಕಾಗಿ ಕ್ಷಮಿಸಿ.'}

WHY = {'English': 'Fixing this is needed before you can start accepting payments.',
 'Hinglish': 'Payments lena shuru karne se pehle ise theek karna zaroori hai.',
 'Hindi': 'पेमेंट लेना शुरू करने से पहले इसे ठीक करना ज़रूरी है।',
 'Marathi': 'पेमेंट घेणे सुरू करण्यापूर्वी हे ठीक करणे आवश्यक आहे.',
 'Tamil': 'பணம் பெறத் தொடங்குவதற்கு முன் இதைச் சரிசெய்வது அவசியம்.',
 'Kannada': 'ಪಾವತಿಗಳನ್ನು ಸ್ವೀಕರಿಸಲು ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು ಇದನ್ನು ಸರಿಪಡಿಸುವುದು ಅಗತ್ಯ.'}

WHY_R13 = {'English': 'Finishing your application is needed before you can start accepting payments.',
 'Hinglish': 'Payments lena shuru karne se pehle application poori karna zaroori hai.',
 'Hindi': 'पेमेंट लेना शुरू करने से पहले आवेदन पूरा करना ज़रूरी है।',
 'Marathi': 'पेमेंट घेणे सुरू करण्यापूर्वी अर्ज पूर्ण करणे आवश्यक आहे.',
 'Tamil': 'பணம் பெறத் தொடங்குவதற்கு முன் விண்ணப்பத்தை முடிப்பது அவசியம்.',
 'Kannada': 'ಪಾವತಿಗಳನ್ನು ಸ್ವೀಕರಿಸಲು ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು ಅರ್ಜಿಯನ್ನು ಪೂರ್ಣಗೊಳಿಸುವುದು ಅಗತ್ಯ.'}

CTA = {'English': 'Continue here: [resume link]',
 'Hinglish': 'Yahan se continue karein: [resume link]',
 'Hindi': 'यहाँ से जारी रखें: [resume link]',
 'Marathi': 'इथून पुढे सुरू ठेवा: [resume link]',
 'Tamil': 'இங்கிருந்து தொடருங்கள்: [resume link]',
 'Kannada': 'ಇಲ್ಲಿಂದ ಮುಂದುವರಿಸಿ: [resume link]'}

HELP = {'English': 'If you need any help, just reply to this message and our team will assist you.',
 'Hinglish': 'Kisi bhi madad ke liye bas is message ka reply karein, hamari team aapki sahayata karegi.',
 'Hindi': 'किसी भी मदद के लिए बस इस संदेश का जवाब दें, हमारी टीम आपकी सहायता करेगी।',
 'Marathi': 'कोणत्याही मदतीसाठी या संदेशाला फक्त उत्तर द्या, आमची टीम तुम्हाला मदत करेल.',
 'Tamil': 'ஏதேனும் உதவி தேவைப்பட்டால் இந்தச் செய்திக்குப் பதிலளியுங்கள், எங்கள் குழு உங்களுக்கு உதவும்.',
 'Kannada': 'ಯಾವುದೇ ಸಹಾಯ ಬೇಕಾದರೆ ಈ ಸಂದೇಶಕ್ಕೆ ಉತ್ತರಿಸಿ, ನಮ್ಮ ತಂಡ ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ.'}

STOP = {'English': 'Reply STOP to stop these messages.',
 'Hinglish': 'In messages ko rokne ke liye STOP likhkar reply karein.',
 'Hindi': 'इन संदेशों को रोकने के लिए STOP लिखकर जवाब दें।',
 'Marathi': 'हे संदेश थांबवण्यासाठी STOP लिहून उत्तर द्या.',
 'Tamil': 'இந்தச் செய்திகளை நிறுத்த STOP என்று பதிலளியுங்கள்.',
 'Kannada': 'ಈ ಸಂದೇಶಗಳನ್ನು ನಿಲ್ಲಿಸಲು STOP ಎಂದು ಉತ್ತರಿಸಿ.'}

SIGN = {'English': 'Razorpay Onboarding Team',
 'Hinglish': 'Razorpay Onboarding Team',
 'Hindi': 'Razorpay ऑनबोर्डिंग टीम',
 'Marathi': 'Razorpay ऑनबोर्डिंग टीम',
 'Tamil': 'Razorpay ஆன்போர்டிங் குழு',
 'Kannada': 'Razorpay ಆನ್\u200cಬೋರ್ಡಿಂಗ್ ತಂಡ'}

SUBJ = {'day0': {'English': 'Your Razorpay application: next step',
          'Hinglish': 'Aapki Razorpay application: agla step',
          'Hindi': 'आपका Razorpay आवेदन: अगला कदम',
          'Marathi': 'तुमचा Razorpay अर्ज: पुढची पायरी',
          'Tamil': 'உங்கள் Razorpay விண்ணப்பம்: அடுத்த படி',
          'Kannada': 'ನಿಮ್ಮ Razorpay ಅರ್ಜಿ: ಮುಂದಿನ ಹಂತ'},
 'day3': {'English': 'A reminder about your Razorpay application',
          'Hinglish': 'Aapki Razorpay application ka reminder',
          'Hindi': 'आपके Razorpay आवेदन के बारे में रिमाइंडर',
          'Marathi': 'तुमच्या Razorpay अर्जाबद्दल एक आठवण',
          'Tamil': 'உங்கள் Razorpay விண்ணப்பம் குறித்த நினைவூட்டல்',
          'Kannada': 'ನಿಮ್ಮ Razorpay ಅರ್ಜಿಯ ಬಗ್ಗೆ ಜ್ಞಾಪನೆ'},
 'day7': {'English': 'Need help with your Razorpay application?',
          'Hinglish': 'Razorpay application mein madad chahiye?',
          'Hindi': 'Razorpay आवेदन में मदद चाहिए?',
          'Marathi': 'Razorpay अर्जासाठी मदत हवी आहे का?',
          'Tamil': 'Razorpay விண்ணப்பத்திற்கு உதவி வேண்டுமா?',
          'Kannada': 'Razorpay ಅರ್ಜಿಗೆ ಸಹಾಯ ಬೇಕೇ?'},
 'plain': {'English': 'Your Razorpay application',
           'Hinglish': 'Aapki Razorpay application',
           'Hindi': 'आपका Razorpay आवेदन',
           'Marathi': 'तुमचा Razorpay अर्ज',
           'Tamil': 'உங்கள் Razorpay விண்ணப்பம்',
           'Kannada': 'ನಿಮ್ಮ Razorpay ಅರ್ಜಿ'}}

BODY = {'R01': {'English': ('The name on your PAN card does not match the business name in your application.',
                     'Please upload the PAN of the business (or of the owner, for a proprietorship) that matches your application. Or correct the business '
                     'name to match your PAN.'),
         'Hinglish': ('Aapke PAN card ka naam application ke business naam se match nahi karta.',
                      'Kripya wo PAN upload karein jiska naam application se match karta ho (business ka PAN, ya proprietorship mein owner ka). Ya business ka '
                      'naam PAN ke hisaab se theek karein.'),
         'Hindi': ('आपके PAN कार्ड पर जो नाम है, वह आवेदन में दिए गए बिज़नेस के नाम से मेल नहीं खाता।',
                   'कृपया वह PAN अपलोड करें जिसका नाम आवेदन से मेल खाता हो (बिज़नेस का PAN, या प्रोप्राइटरशिप हो तो मालिक का PAN)। या बिज़नेस का नाम PAN के '
                   'अनुसार ठीक कर दें।'),
         'Marathi': ('तुमच्या PAN कार्डवरील नाव अर्जात दिलेल्या व्यवसायाच्या नावाशी जुळत नाही.',
                     'कृपया अर्जाच्या नावाशी जुळणारे PAN अपलोड करा (व्यवसायाचे PAN, किंवा प्रोप्रायटरशिप असल्यास मालकाचे PAN). किंवा व्यवसायाचे नाव PAN नुसार '
                     'दुरुस्त करा.'),
         'Tamil': ('உங்கள் PAN அட்டையில் உள்ள பெயர், விண்ணப்பத்தில் கொடுத்த வணிகப் பெயருடன் பொருந்தவில்லை.',
                   'விண்ணப்பத்துடன் பொருந்தும் PAN ஐ பதிவேற்றவும் (வணிகத்தின் PAN, அல்லது தனியுரிமை நிறுவனமாக இருந்தால் உரிமையாளரின் PAN). அல்லது வணிகப் பெயரை '
                   'PAN படி திருத்தவும்.'),
         'Kannada': ('ನಿಮ್ಮ PAN ಕಾರ್ಡ್\u200cನಲ್ಲಿರುವ ಹೆಸರು ಅರ್ಜಿಯಲ್ಲಿ ನೀಡಿದ ವ್ಯಾಪಾರದ ಹೆಸರಿಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತಿಲ್ಲ.',
                     'ಅರ್ಜಿಗೆ ಹೊಂದುವ PAN ಅನ್ನು ಅಪ್\u200cಲೋಡ್ ಮಾಡಿ (ವ್ಯಾಪಾರದ PAN, ಅಥವಾ ಏಕಮಾಲೀಕತ್ವವಾಗಿದ್ದರೆ ಮಾಲೀಕರ PAN). ಅಥವಾ ವ್ಯಾಪಾರದ ಹೆಸರನ್ನು PAN ಪ್ರಕಾರ '
                     'ಸರಿಪಡಿಸಿ.')},
 'R02': {'English': ('We could not validate your GST details. The GSTIN may be wrong, inactive, or linked to a different legal name or address.',
                     'Please enter the correct GSTIN. Or upload a current GST certificate that matches your legal name and address.'),
         'Hinglish': ('Hum aapki GST details verify nahi kar paaye. GSTIN galat, inactive, ya kisi aur legal naam ya address se juda ho sakta hai.',
                      'Kripya sahi GSTIN daalein. Ya aisa current GST certificate upload karein jo aapke legal naam aur address se match karta ho.'),
         'Hindi': ('हम आपकी GST जानकारी सत्यापित नहीं कर पाए। GSTIN गलत, निष्क्रिय, या किसी और कानूनी नाम या पते से जुड़ा हो सकता है।',
                   'कृपया सही GSTIN दर्ज करें। या ऐसा वर्तमान GST प्रमाणपत्र अपलोड करें जो आपके कानूनी नाम और पते से मेल खाता हो।'),
         'Marathi': ('आम्ही तुमची GST माहिती पडताळू शकलो नाही. GSTIN चुकीचा, निष्क्रिय किंवा दुसऱ्या कायदेशीर नावाशी किंवा पत्त्याशी जोडलेला असू शकतो.',
                     'कृपया योग्य GSTIN टाका. किंवा तुमच्या कायदेशीर नावाशी आणि पत्त्याशी जुळणारे चालू GST प्रमाणपत्र अपलोड करा.'),
         'Tamil': ('உங்கள் GST விவரங்களை எங்களால் சரிபார்க்க முடியவில்லை. GSTIN தவறாக, செயலற்றதாக அல்லது வேறு பெயர் அல்லது முகவரியுடன் இணைந்ததாக இருக்கலாம்.',
                   'சரியான GSTIN ஐ உள்ளிடவும். அல்லது உங்கள் பெயர், முகவரியுடன் பொருந்தும் தற்போதைய GST சான்றிதழைப் பதிவேற்றவும்.'),
         'Kannada': ('ನಿಮ್ಮ GST ವಿವರಗಳನ್ನು ನಾವು ಪರಿಶೀಲಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. GSTIN ತಪ್ಪಾಗಿರಬಹುದು, ನಿಷ್ಕ್ರಿಯವಾಗಿರಬಹುದು ಅಥವಾ ಬೇರೆ ಕಾನೂನುಬದ್ಧ ಹೆಸರು ಅಥವಾ ವಿಳಾಸಕ್ಕೆ '
                     'ಸೇರಿರಬಹುದು.',
                     'ಸರಿಯಾದ GSTIN ನಮೂದಿಸಿ. ಅಥವಾ ನಿಮ್ಮ ಕಾನೂನುಬದ್ಧ ಹೆಸರು ಮತ್ತು ವಿಳಾಸಕ್ಕೆ ಹೊಂದುವ ಪ್ರಸ್ತುತ GST ಪ್ರಮಾಣಪತ್ರವನ್ನು ಅಪ್\u200cಲೋಡ್ ಮಾಡಿ.')},
 'R03': {'English': ('The name on your bank account does not match your business or PAN name.',
                     "Please use a current account in the business name (the owner's name for a proprietorship). Or upload a bank letter or cancelled cheque "
                     'that shows the matching name.'),
         'Hinglish': ('Aapke bank account ka naam business ya PAN ke naam se match nahi kar raha.',
                      'Kripya business ke naam ka current account use karein (proprietorship mein owner ke naam ka). Ya bank letter ya cancelled cheque upload '
                      'karein jisme sahi naam dikh raha ho.'),
         'Hindi': ('आपके बैंक खाते का नाम बिज़नेस या PAN के नाम से मेल नहीं खा रहा।',
                   'कृपया बिज़नेस के नाम का करंट अकाउंट इस्तेमाल करें (प्रोप्राइटरशिप में मालिक के नाम का)। या बैंक पत्र या कैंसल्ड चेक अपलोड करें जिसमें सही '
                   'नाम दिख रहा हो।'),
         'Marathi': ('तुमच्या बँक खात्यावरील नाव व्यवसायाच्या किंवा PAN वरील नावाशी जुळत नाही.',
                     'कृपया व्यवसायाच्या नावाचे करंट अकाउंट वापरा (प्रोप्रायटरशिपमध्ये मालकाच्या नावाचे). किंवा योग्य नाव दिसणारे बँक पत्र किंवा रद्द केलेला '
                     'चेक अपलोड करा.'),
         'Tamil': ('உங்கள் வங்கிக் கணக்கில் உள்ள பெயர், வணிகம் அல்லது PAN பெயருடன் பொருந்தவில்லை.',
                   'வணிகப் பெயரில் உள்ள நடப்புக் கணக்கைப் பயன்படுத்தவும் (தனியுரிமை நிறுவனத்தில் உரிமையாளர் பெயரில்). அல்லது சரியான பெயருடன் வங்கிக் கடிதம் '
                   'அல்லது ரத்து செய்த காசோலையைப் பதிவேற்றவும்.'),
         'Kannada': ('ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಯಲ್ಲಿರುವ ಹೆಸರು ವ್ಯಾಪಾರ ಅಥವಾ PAN ಹೆಸರಿಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತಿಲ್ಲ.',
                     'ವ್ಯಾಪಾರದ ಹೆಸರಿನ ಚಾಲ್ತಿ ಖಾತೆಯನ್ನು ಬಳಸಿ (ಏಕಮಾಲೀಕತ್ವದಲ್ಲಿ ಮಾಲೀಕರ ಹೆಸರಿನದು). ಅಥವಾ ಸರಿಯಾದ ಹೆಸರು ಕಾಣುವ ಬ್ಯಾಂಕ್ ಪತ್ರ ಅಥವಾ ರದ್ದುಗೊಳಿಸಿದ ಚೆಕ್ '
                     'ಅಪ್\u200cಲೋಡ್ ಮಾಡಿ.')},
 'R04': {'English': ('We could not verify your bank account with the small test credit.',
                     'Please re-enter the account number and IFSC carefully. Also check that the account is active and can receive credits.'),
         'Hinglish': ('Hum chhote test credit se aapka bank account verify nahi kar paaye.',
                      'Kripya account number aur IFSC dhyan se dobara daalein. Saath hi check karein ki account active hai aur usme paise aa sakte hain.'),
         'Hindi': ('हम छोटे टेस्ट क्रेडिट से आपका बैंक खाता सत्यापित नहीं कर पाए।',
                   'कृपया खाता संख्या और IFSC ध्यान से दोबारा दर्ज करें। साथ ही जाँच लें कि खाता चालू है और उसमें पैसे आ सकते हैं।'),
         'Marathi': ('आम्ही छोट्या चाचणी रकमेद्वारे तुमचे बँक खाते पडताळू शकलो नाही.',
                     'कृपया खाते क्रमांक आणि IFSC काळजीपूर्वक पुन्हा टाका. तसेच खाते सुरू असून त्यात पैसे जमा होऊ शकतात याची खात्री करा.'),
         'Tamil': ('சிறிய சோதனைப் பணப் பரிமாற்றம் மூலம் உங்கள் வங்கிக் கணக்கை எங்களால் சரிபார்க்க முடியவில்லை.',
                   'கணக்கு எண் மற்றும் IFSC ஐ கவனமாக மீண்டும் உள்ளிடவும். மேலும் கணக்கு செயலில் உள்ளதா, பணம் வரவு வைக்க முடியுமா என்பதையும் சரிபார்க்கவும்.'),
         'Kannada': ('ಸಣ್ಣ ಪರೀಕ್ಷಾ ಜಮಾ ಮೂಲಕ ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಯನ್ನು ನಾವು ಪರಿಶೀಲಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ.',
                     'ಖಾತೆ ಸಂಖ್ಯೆ ಮತ್ತು IFSC ಅನ್ನು ಎಚ್ಚರಿಕೆಯಿಂದ ಮತ್ತೆ ನಮೂದಿಸಿ. ಜೊತೆಗೆ ಖಾತೆ ಸಕ್ರಿಯವಾಗಿದೆಯೇ, ಹಣ ಜಮಾ ಆಗಬಹುದೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.')},
 'R05': {'English': ('We could not read your document. It may be blurred, cropped or password-protected.',
                     'Please upload a clear, full-page colour scan in PDF, JPG or PNG under 5 MB.'),
         'Hinglish': ('Hum aapka document padh nahi paaye. Wo blur, cropped ya password-protected ho sakta hai.',
                      'Kripya saaf, poore page ka colour scan PDF, JPG ya PNG mein upload karein, 5 MB se chhota.'),
         'Hindi': ('हम आपका दस्तावेज़ पढ़ नहीं पाए। वह धुंधला, कटा हुआ या पासवर्ड वाला हो सकता है।',
                   'कृपया साफ़, पूरे पन्ने का रंगीन स्कैन PDF, JPG या PNG में अपलोड करें, 5 MB से छोटा।'),
         'Marathi': ('आम्ही तुमचे कागदपत्र वाचू शकलो नाही. ते अस्पष्ट, कापलेले किंवा पासवर्ड असलेले असू शकते.',
                     'कृपया स्पष्ट, पूर्ण पानाचे रंगीत स्कॅन PDF, JPG किंवा PNG मध्ये अपलोड करा, 5 MB पेक्षा लहान.'),
         'Tamil': ('உங்கள் ஆவணத்தை எங்களால் படிக்க முடியவில்லை. அது மங்கலாக, வெட்டப்பட்டதாக அல்லது கடவுச்சொல் உள்ளதாக இருக்கலாம்.',
                   'தெளிவான, முழுப் பக்க வண்ண ஸ்கேனை PDF, JPG அல்லது PNG வடிவில், 5 MB க்கும் குறைவாகப் பதிவேற்றவும்.'),
         'Kannada': ('ನಿಮ್ಮ ದಾಖಲೆಯನ್ನು ನಮಗೆ ಓದಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ಅದು ಮಸುಕಾಗಿರಬಹುದು, ಕತ್ತರಿಸಲ್ಪಟ್ಟಿರಬಹುದು ಅಥವಾ ಪಾಸ್\u200cವರ್ಡ್ ಇರಬಹುದು.',
                     'ಸ್ಪಷ್ಟವಾದ, ಪೂರ್ಣ ಪುಟದ ಬಣ್ಣದ ಸ್ಕ್ಯಾನ್ ಅನ್ನು PDF, JPG ಅಥವಾ PNG ರೂಪದಲ್ಲಿ, 5 MB ಗಿಂತ ಚಿಕ್ಕದಾಗಿ ಅಪ್\u200cಲೋಡ್ ಮಾಡಿ.')},
 'R06': {'English': ('Your website or app is missing some required pages.',
                     'Please add these pages with working links: Terms & Conditions, Privacy Policy, Refund/Cancellation Policy and Contact details. Then '
                     'submit your website link again.'),
         'Hinglish': ('Aapki website ya app mein kuch zaroori pages nahi hain.',
                      'Kripya ye pages working links ke saath jodein: Terms & Conditions, Privacy Policy, Refund/Cancellation Policy aur Contact details. Phir '
                      'website ka link dobara submit karein.'),
         'Hindi': ('आपकी वेबसाइट या ऐप में कुछ ज़रूरी पेज नहीं हैं।',
                   'कृपया ये पेज चालू लिंक के साथ जोड़ें: Terms & Conditions, Privacy Policy, Refund/Cancellation Policy और संपर्क जानकारी। फिर वेबसाइट का '
                   'लिंक दोबारा जमा करें।'),
         'Marathi': ('तुमच्या वेबसाइट किंवा अॅपमध्ये काही आवश्यक पाने नाहीत.',
                     'कृपया ही पाने चालू लिंकसह जोडा: Terms & Conditions, Privacy Policy, Refund/Cancellation Policy आणि संपर्क माहिती. मग वेबसाइटची लिंक '
                     'पुन्हा सादर करा.'),
         'Tamil': ('உங்கள் இணையதளம் அல்லது செயலியில் சில தேவையான பக்கங்கள் இல்லை.',
                   'இந்தப் பக்கங்களை வேலை செய்யும் இணைப்புகளுடன் சேர்க்கவும்: Terms & Conditions, Privacy Policy, Refund/Cancellation Policy, தொடர்பு '
                   'விவரங்கள். பின்னர் இணைப்பை மீண்டும் சமர்ப்பிக்கவும்.'),
         'Kannada': ('ನಿಮ್ಮ ವೆಬ್\u200cಸೈಟ್ ಅಥವಾ ಆ್ಯಪ್\u200cನಲ್ಲಿ ಕೆಲವು ಅಗತ್ಯ ಪುಟಗಳು ಇಲ್ಲ.',
                     'ಈ ಪುಟಗಳನ್ನು ಕೆಲಸ ಮಾಡುವ ಲಿಂಕ್\u200cಗಳೊಂದಿಗೆ ಸೇರಿಸಿ: Terms & Conditions, Privacy Policy, Refund/Cancellation Policy ಮತ್ತು ಸಂಪರ್ಕ ವಿವರಗಳು. '
                     'ನಂತರ ವೆಬ್\u200cಸೈಟ್ ಲಿಂಕ್ ಅನ್ನು ಮತ್ತೆ ಸಲ್ಲಿಸಿ.')},
 'R07': {'English': ('We could not review your website. It is not live, or it needs a login to see products and prices.',
                     'Please make the website open to everyone, with products, prices and contact details visible. Then submit it again.'),
         'Hinglish': ('Hum aapki website review nahi kar paaye. Wo live nahi hai, ya products aur prices dekhne ke liye login maangti hai.',
                      'Kripya website ko sabke liye khula rakhein, jisme products, prices aur contact details dikhein. Phir dobara submit karein.'),
         'Hindi': ('हम आपकी वेबसाइट की समीक्षा नहीं कर पाए। वह चालू नहीं है, या प्रोडक्ट और कीमतें देखने के लिए लॉगिन माँगती है।',
                   'कृपया वेबसाइट को सबके लिए खुला रखें, जिसमें प्रोडक्ट, कीमतें और संपर्क जानकारी दिखें। फिर दोबारा जमा करें।'),
         'Marathi': ('आम्ही तुमच्या वेबसाइटचे पुनरावलोकन करू शकलो नाही. ती सुरू नाही, किंवा उत्पादने आणि किमती पाहण्यासाठी लॉगिन मागते.',
                     'कृपया वेबसाइट सर्वांसाठी खुली ठेवा, ज्यात उत्पादने, किमती आणि संपर्क माहिती दिसेल. मग पुन्हा सादर करा.'),
         'Tamil': ('இணையதளத்தை எங்களால் மதிப்பாய்வு செய்ய முடியவில்லை. அது இயங்கவில்லை, அல்லது பொருட்களைப் பார்க்க உள்நுழைவு கேட்கிறது.',
                   'இணையதளத்தை அனைவரும் பார்க்கும்படி திறந்து வைக்கவும்; பொருட்கள், விலைகள், தொடர்பு விவரங்கள் தெரிய வேண்டும். மீண்டும் சமர்ப்பிக்கவும்.'),
         'Kannada': ('ನಿಮ್ಮ ವೆಬ್\u200cಸೈಟ್ ಅನ್ನು ನಮಗೆ ಪರಿಶೀಲಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ಅದು ಚಾಲ್ತಿಯಲ್ಲಿಲ್ಲ, ಅಥವಾ ಉತ್ಪನ್ನಗಳು ಮತ್ತು ಬೆಲೆಗಳನ್ನು ನೋಡಲು ಲಾಗಿನ್ ಕೇಳುತ್ತದೆ.',
                     'ವೆಬ್\u200cಸೈಟ್ ಎಲ್ಲರಿಗೂ ತೆರೆದಿರುವಂತೆ ಮಾಡಿ, ಉತ್ಪನ್ನಗಳು, ಬೆಲೆಗಳು ಮತ್ತು ಸಂಪರ್ಕ ವಿವರಗಳು ಕಾಣಿಸಬೇಕು. ನಂತರ ಮತ್ತೆ ಸಲ್ಲಿಸಿ.')},
 'R08': {'English': ('Your address proof is missing, out of date, or shows a different address from your application.',
                     'Please upload a recent utility bill, rent agreement or other valid address proof. It should match the address in your application.'),
         'Hinglish': ('Aapka address proof nahi mila, purana hai, ya application ke address se alag address dikha raha hai.',
                      'Kripya haal ka utility bill, rent agreement ya koi aur valid address proof upload karein. Wo application ke address se match hona '
                      'chahiye.'),
         'Hindi': ('आपका पते का प्रमाण नहीं मिला, पुराना है, या आवेदन के पते से अलग पता दिखा रहा है।',
                   'कृपया हाल का बिजली या पानी का बिल, किराया समझौता या कोई और मान्य पते का प्रमाण अपलोड करें। वह आवेदन के पते से मेल खाना चाहिए।'),
         'Marathi': ('तुमचा पत्त्याचा पुरावा सापडला नाही, जुना आहे, किंवा अर्जातील पत्त्यापेक्षा वेगळा पत्ता दाखवतो.',
                     'कृपया अलीकडचे वीज बिल, भाडे करार किंवा इतर वैध पत्त्याचा पुरावा अपलोड करा. तो अर्जातील पत्त्याशी जुळला पाहिजे.'),
         'Tamil': ('உங்கள் முகவரிச் சான்று இல்லை, பழையது, அல்லது விண்ணப்பத்தில் உள்ள முகவரியிலிருந்து வேறுபடுகிறது.',
                   'சமீபத்திய மின்கட்டண ரசீது, வாடகை ஒப்பந்தம் அல்லது வேறு செல்லுபடியாகும் முகவரிச் சான்றைப் பதிவேற்றவும். அது விண்ணப்ப முகவரியுடன் பொருந்த '
                   'வேண்டும்.'),
         'Kannada': ('ನಿಮ್ಮ ವಿಳಾಸ ಪುರಾವೆ ಇಲ್ಲ, ಹಳೆಯದಾಗಿದೆ, ಅಥವಾ ಅರ್ಜಿಯಲ್ಲಿನ ವಿಳಾಸಕ್ಕಿಂತ ಬೇರೆ ವಿಳಾಸ ತೋರಿಸುತ್ತಿದೆ.',
                     'ಇತ್ತೀಚಿನ ವಿದ್ಯುತ್ ಬಿಲ್, ಬಾಡಿಗೆ ಒಪ್ಪಂದ ಅಥವಾ ಬೇರೆ ಮಾನ್ಯ ವಿಳಾಸ ಪುರಾವೆಯನ್ನು ಅಪ್\u200cಲೋಡ್ ಮಾಡಿ. ಅದು ಅರ್ಜಿಯ ವಿಳಾಸಕ್ಕೆ ಹೊಂದಿಕೆಯಾಗಬೇಕು.')},
 'R09': {'English': ('The ID of your authorised signatory or director is missing, or its details do not match your application.',
                     'Please upload a valid ID of the authorised signatory. Make sure the name and date of birth match your application.'),
         'Hinglish': ('Aapke authorised signatory ya director ka ID nahi mila, ya uski details application se match nahi karti.',
                      'Kripya authorised signatory ka valid ID upload karein. Dhyan rakhein ki naam aur date of birth application se match hon.'),
         'Hindi': ('आपके अधिकृत हस्ताक्षरकर्ता या डायरेक्टर का पहचान पत्र नहीं मिला, या उसकी जानकारी आवेदन से मेल नहीं खाती।',
                   'कृपया अधिकृत हस्ताक्षरकर्ता का मान्य पहचान पत्र अपलोड करें। ध्यान रखें कि नाम और जन्मतिथि आवेदन से मेल खाएँ।'),
         'Marathi': ('तुमच्या अधिकृत स्वाक्षरीकर्त्याचे किंवा संचालकाचे ओळखपत्र सापडले नाही, किंवा त्यातील माहिती अर्जाशी जुळत नाही.',
                     'कृपया अधिकृत स्वाक्षरीकर्त्याचे वैध ओळखपत्र अपलोड करा. नाव व जन्मतारीख अर्जाशी जुळतील याची खात्री करा.'),
         'Tamil': ('கையொப்பதாரர் அல்லது இயக்குநரின் அடையாளச் சான்று இல்லை, அல்லது அதிலுள்ள விவரங்கள் விண்ணப்பத்துடன் பொருந்தவில்லை.',
                   'கையொப்பதாரரின் செல்லுபடியாகும் அடையாளச் சான்றைப் பதிவேற்றவும். பெயர், பிறந்த தேதி விண்ணப்பத்துடன் பொருந்த வேண்டும்.'),
         'Kannada': ('ನಿಮ್ಮ ಅಧಿಕೃತ ಸಹಿದಾರ ಅಥವಾ ನಿರ್ದೇಶಕರ ಗುರುತಿನ ಚೀಟಿ ಇಲ್ಲ, ಅಥವಾ ಅದರ ವಿವರಗಳು ಅರ್ಜಿಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತಿಲ್ಲ.',
                     'ಅಧಿಕೃತ ಸಹಿದಾರರ ಮಾನ್ಯ ಗುರುತಿನ ಚೀಟಿಯನ್ನು ಅಪ್\u200cಲೋಡ್ ಮಾಡಿ. ಹೆಸರು ಮತ್ತು ಜನ್ಮ ದಿನಾಂಕ ಅರ್ಜಿಗೆ ಹೊಂದಿಕೆಯಾಗುವಂತೆ ನೋಡಿಕೊಳ್ಳಿ.')},
 'R11': {'English': ('The business category you selected is different from what your website sells.',
                     'Please select the correct category. Or share a short note with evidence explaining your business model, for a second review.'),
         'Hinglish': ('Aapne jo business category chuni hai wo aapki website par bik rahe samaan se alag hai.',
                      'Kripya sahi category chunein. Ya apne business model ka chhota note aur proof share karein, taaki dobara review ho sake.'),
         'Hindi': ('आपने जो बिज़नेस श्रेणी चुनी है वह आपकी वेबसाइट पर बिकने वाली चीज़ों से अलग है।',
                   'कृपया सही श्रेणी चुनें। या अपने बिज़नेस मॉडल पर एक छोटा नोट और सबूत साझा करें, ताकि दोबारा समीक्षा हो सके।'),
         'Marathi': ('तुम्ही निवडलेली व्यवसाय श्रेणी तुमच्या वेबसाइटवर विकल्या जाणाऱ्या गोष्टींपेक्षा वेगळी आहे.',
                     'कृपया योग्य श्रेणी निवडा. किंवा तुमच्या व्यवसाय मॉडेलबद्दल छोटी नोंद आणि पुरावा द्या, म्हणजे पुन्हा पुनरावलोकन करता येईल.'),
         'Tamil': ('நீங்கள் தேர்ந்தெடுத்த வணிக வகை, உங்கள் இணையதளத்தில் விற்கப்படுவதிலிருந்து வேறுபடுகிறது.',
                   'சரியான வகையைத் தேர்ந்தெடுக்கவும். அல்லது உங்கள் வணிக முறை குறித்த சிறு குறிப்பையும் ஆதாரத்தையும் பகிரவும், இரண்டாவது மதிப்பாய்வுக்காக.'),
         'Kannada': ('ನೀವು ಆಯ್ಕೆ ಮಾಡಿದ ವ್ಯಾಪಾರ ವರ್ಗ ನಿಮ್ಮ ವೆಬ್\u200cಸೈಟ್\u200cನಲ್ಲಿ ಮಾರಾಟವಾಗುವುದಕ್ಕಿಂತ ಬೇರೆಯಾಗಿದೆ.',
                     'ಸರಿಯಾದ ವರ್ಗವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ. ಅಥವಾ ನಿಮ್ಮ ವ್ಯಾಪಾರ ಮಾದರಿಯ ಬಗ್ಗೆ ಸಣ್ಣ ಟಿಪ್ಪಣಿ ಮತ್ತು ಪುರಾವೆ ಹಂಚಿಕೊಳ್ಳಿ, ಎರಡನೇ ಪರಿಶೀಲನೆಗಾಗಿ.')},
 'R13': {'English': ('You stopped at the {step} step.', 'You can pick up from where you left off using the link below.'),
         'Hinglish': ('Aap {step} step par ruk gaye the.', 'Neeche diye link se aap wahin se aage badh sakte hain.'),
         'Hindi': ('आप {step} चरण पर रुक गए थे।', 'नीचे दिए लिंक से आप वहीं से आगे बढ़ सकते हैं।'),
         'Marathi': ('तुम्ही {step} टप्प्यावर थांबला होता.', 'खालील लिंकवरून तुम्ही तिथूनच पुढे जाऊ शकता.'),
         'Tamil': ('நீங்கள் {step} படியில் நிறுத்திவிட்டீர்கள்.', 'கீழே உள்ள இணைப்பின் மூலம் நீங்கள் நிறுத்திய இடத்திலிருந்தே தொடரலாம்.'),
         'Kannada': ('ನೀವು {step} ಹಂತದಲ್ಲಿ ನಿಲ್ಲಿಸಿದ್ದೀರಿ.', 'ಕೆಳಗಿನ ಲಿಂಕ್ ಮೂಲಕ ನೀವು ನಿಲ್ಲಿಸಿದ ಜಾಗದಿಂದಲೇ ಮುಂದುವರಿಸಬಹುದು.')}}

SHORT = {'R01': {'English': 'the PAN name match',
         'Hinglish': 'PAN name match',
         'Hindi': 'PAN नाम मिलान',
         'Marathi': 'PAN नावाची जुळवणी',
         'Tamil': 'PAN பெயர் பொருத்தம்',
         'Kannada': 'PAN ಹೆಸರಿನ ಹೊಂದಾಣಿಕೆ'},
 'R02': {'English': 'your GST details',
         'Hinglish': 'GST details',
         'Hindi': 'GST जानकारी',
         'Marathi': 'तुमची GST माहिती',
         'Tamil': 'உங்கள் GST விவரங்கள்',
         'Kannada': 'ನಿಮ್ಮ GST ವಿವರಗಳು'},
 'R03': {'English': 'the bank account name',
         'Hinglish': 'bank account name',
         'Hindi': 'बैंक खाता नाम',
         'Marathi': 'बँक खात्यावरील नाव',
         'Tamil': 'வங்கிக் கணக்கு பெயர்',
         'Kannada': 'ಬ್ಯಾಂಕ್ ಖಾತೆಯ ಹೆಸರು'},
 'R04': {'English': 'your bank account verification',
         'Hinglish': 'bank account verification',
         'Hindi': 'बैंक खाता सत्यापन',
         'Marathi': 'बँक खाते पडताळणी',
         'Tamil': 'வங்கிக் கணக்கு சரிபார்ப்பு',
         'Kannada': 'ಬ್ಯಾಂಕ್ ಖಾತೆ ಪರಿಶೀಲನೆ'},
 'R05': {'English': 'a clearer document',
         'Hinglish': 'saaf document',
         'Hindi': 'साफ़ दस्तावेज़',
         'Marathi': 'अधिक स्पष्ट कागदपत्र',
         'Tamil': 'தெளிவான ஆவணம்',
         'Kannada': 'ಹೆಚ್ಚು ಸ್ಪಷ್ಟ ದಾಖಲೆ'},
 'R06': {'English': 'your website policy pages',
         'Hinglish': 'website policy pages',
         'Hindi': 'वेबसाइट पॉलिसी पेज',
         'Marathi': 'वेबसाइटची पॉलिसी पाने',
         'Tamil': 'இணையதளக் கொள்கைப் பக்கங்கள்',
         'Kannada': 'ವೆಬ್\u200cಸೈಟ್ ನೀತಿ ಪುಟಗಳು'},
 'R07': {'English': 'your website access',
         'Hinglish': 'website access',
         'Hindi': 'वेबसाइट एक्सेस',
         'Marathi': 'वेबसाइटचा प्रवेश',
         'Tamil': 'இணையதள அணுகல்',
         'Kannada': 'ವೆಬ್\u200cಸೈಟ್ ಪ್ರವೇಶ'},
 'R08': {'English': 'your address proof',
         'Hinglish': 'address proof',
         'Hindi': 'पते का प्रमाण',
         'Marathi': 'पत्त्याचा पुरावा',
         'Tamil': 'முகவரிச் சான்று',
         'Kannada': 'ವಿಳಾಸ ಪುರಾವೆ'},
 'R09': {'English': 'the signatory ID',
         'Hinglish': 'signatory ID',
         'Hindi': 'हस्ताक्षरकर्ता ID',
         'Marathi': 'स्वाक्षरीकर्त्याचे ओळखपत्र',
         'Tamil': 'கையொப்பதாரர் அடையாளச் சான்று',
         'Kannada': 'ಸಹಿದಾರರ ಗುರುತಿನ ಚೀಟಿ'},
 'R11': {'English': 'your business category',
         'Hinglish': 'business category',
         'Hindi': 'बिज़नेस श्रेणी',
         'Marathi': 'व्यवसाय श्रेणी',
         'Tamil': 'வணிக வகை',
         'Kannada': 'ವ್ಯಾಪಾರ ವರ್ಗ'}}

D3 = {'English': 'a quick reminder: your Razorpay application is still waiting on {s}. Continue here: [resume link]',
 'Hinglish': 'ek chhota reminder: aapki Razorpay application mein abhi {s} pending hai. Yahan se continue karein: [resume link]',
 'Hindi': 'एक छोटा रिमाइंडर: आपके Razorpay आवेदन में अभी {s} बाकी है। यहाँ से जारी रखें: [resume link]',
 'Marathi': 'एक छोटीशी आठवण: तुमचा Razorpay अर्ज अजूनही यासाठी थांबला आहे: {s}. इथून पुढे सुरू ठेवा: [resume link]',
 'Tamil': 'ஒரு சிறிய நினைவூட்டல்: உங்கள் Razorpay விண்ணப்பம் இன்னும் இதற்காகக் காத்திருக்கிறது: {s}. இங்கிருந்து தொடருங்கள்: [resume link]',
 'Kannada': 'ಒಂದು ಸಣ್ಣ ಜ್ಞಾಪನೆ: ನಿಮ್ಮ Razorpay ಅರ್ಜಿ ಇನ್ನೂ ಇದಕ್ಕಾಗಿ ಕಾಯುತ್ತಿದೆ: {s}. ಇಲ್ಲಿಂದ ಮುಂದುವರಿಸಿ: [resume link]'}

D3_R13 = {'English': 'a quick reminder: your Razorpay application is waiting for you at the {step} step. Continue here: [resume link]',
 'Hinglish': 'ek chhota reminder: aapki Razorpay application {step} step par aapka intezaar kar rahi hai. Yahan se continue karein: [resume link]',
 'Hindi': 'एक छोटा रिमाइंडर: आपका Razorpay आवेदन {step} चरण पर आपका इंतज़ार कर रहा है। यहाँ से जारी रखें: [resume link]',
 'Marathi': 'एक छोटीशी आठवण: तुमचा Razorpay अर्ज {step} टप्प्यावर तुमची वाट पाहत आहे. इथून पुढे सुरू ठेवा: [resume link]',
 'Tamil': 'ஒரு சிறிய நினைவூட்டல்: உங்கள் Razorpay விண்ணப்பம் {step} படியில் உங்களுக்காகக் காத்திருக்கிறது. இங்கிருந்து தொடருங்கள்: [resume link]',
 'Kannada': 'ಒಂದು ಸಣ್ಣ ಜ್ಞಾಪನೆ: ನಿಮ್ಮ Razorpay ಅರ್ಜಿ {step} ಹಂತದಲ್ಲಿ ನಿಮಗಾಗಿ ಕಾಯುತ್ತಿದೆ. ಇಲ್ಲಿಂದ ಮುಂದುವರಿಸಿ: [resume link]'}

D7 = {'English': 'need a hand with {s}? Reply to this message and our team will help you finish. Continue here: [resume link]',
 'Hinglish': '{s} mein madad chahiye? Is message ka reply karein, hamari team aapko poora karne mein madad karegi. Yahan se continue karein: [resume link]',
 'Hindi': '{s} में मदद चाहिए? इस संदेश का जवाब दें, हमारी टीम आपको पूरा करने में मदद करेगी। यहाँ से जारी रखें: [resume link]',
 'Marathi': '{s}: मदत हवी आहे का? या संदेशाला उत्तर द्या, आमची टीम तुम्हाला पूर्ण करण्यात मदत करेल. इथून पुढे सुरू ठेवा: [resume link]',
 'Tamil': '{s}: உதவி வேண்டுமா? இந்தச் செய்திக்குப் பதிலளியுங்கள், முடிக்க எங்கள் குழு உங்களுக்கு உதவும். இங்கிருந்து தொடருங்கள்: [resume link]',
 'Kannada': '{s}: ಸಹಾಯ ಬೇಕೇ? ಈ ಸಂದೇಶಕ್ಕೆ ಉತ್ತರಿಸಿ, ಪೂರ್ಣಗೊಳಿಸಲು ನಮ್ಮ ತಂಡ ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ. ಇಲ್ಲಿಂದ ಮುಂದುವರಿಸಿ: [resume link]'}

CLOSE = {'English': 'Dear Valued Merchant, thank you for applying to Razorpay, and for the time you spent on your application. After review, we are sorry to say that '
            'we are unable to support this type of business, so we have closed your application. We truly appreciate your interest in Razorpay, and we wish '
            'you the very best for your business.',
 'Hinglish': 'Dear Valued Merchant, Razorpay mein apply karne ke liye aur apni application par samay dene ke liye dhanyavaad. Review ke baad hume afsos hai ki '
             'hum is type ke business ko support nahi kar sakte, isliye humne aapki application band kar di hai. Razorpay mein aapki ruchi ke liye hum '
             'sachmuch aabhari hain, aur aapke business ke liye hamari shubhkamnayein.',
 'Hindi': 'आदरणीय व्यापारी, Razorpay में आवेदन करने और अपने आवेदन पर समय देने के लिए धन्यवाद। समीक्षा के बाद हमें खेद है कि हम इस प्रकार के बिज़नेस को सपोर्ट '
          'नहीं कर सकते, इसलिए हमने आपका आवेदन बंद कर दिया है। Razorpay में आपकी रुचि के लिए हम सचमुच आभारी हैं, और आपके बिज़नेस के लिए हमारी हार्दिक '
          'शुभकामनाएँ।',
 'Marathi': 'आदरणीय व्यापारी, Razorpay मध्ये अर्ज केल्याबद्दल आणि तुमच्या अर्जासाठी वेळ दिल्याबद्दल धन्यवाद. पुनरावलोकनानंतर, आम्हाला खेद वाटतो की आम्ही या '
            'प्रकारच्या व्यवसायाला समर्थन देऊ शकत नाही, त्यामुळे आम्ही तुमचा अर्ज बंद केला आहे. Razorpay मधील तुमच्या आवडीबद्दल आम्ही खरोखर आभारी आहोत, आणि '
            'तुमच्या व्यवसायासाठी आमच्या मनःपूर्वक शुभेच्छा.',
 'Tamil': 'மதிப்பிற்குரிய வணிகரே, Razorpay-ல் விண்ணப்பித்ததற்கும், உங்கள் விண்ணப்பத்திற்காக நேரம் செலவிட்டதற்கும் நன்றி. மதிப்பாய்வுக்குப் பிறகு, இந்த வகை '
          'வணிகத்தை எங்களால் ஆதரிக்க முடியாது என்பதற்கு வருந்துகிறோம், எனவே உங்கள் விண்ணப்பத்தை மூடியுள்ளோம். Razorpay மீதான உங்கள் ஆர்வத்திற்கு நாங்கள் '
          'உண்மையாக நன்றி கூறுகிறோம், உங்கள் வணிகம் சிறக்க வாழ்த்துகிறோம்.',
 'Kannada': 'ಗೌರವಾನ್ವಿತ ವ್ಯಾಪಾರಿಗಳೇ, Razorpay ಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿದ್ದಕ್ಕೆ ಮತ್ತು ನಿಮ್ಮ ಅರ್ಜಿಗಾಗಿ ಸಮಯ ನೀಡಿದ್ದಕ್ಕೆ ಧನ್ಯವಾದಗಳು. ಪರಿಶೀಲನೆಯ ನಂತರ, ಈ ರೀತಿಯ ವ್ಯಾಪಾರವನ್ನು '
            'ಬೆಂಬಲಿಸಲು ನಮಗೆ ಸಾಧ್ಯವಿಲ್ಲ ಎಂದು ತಿಳಿಸಲು ಕ್ಷಮಿಸಿ, ಆದ್ದರಿಂದ ನಿಮ್ಮ ಅರ್ಜಿಯನ್ನು ಮುಚ್ಚಿದ್ದೇವೆ. Razorpay ಮೇಲಿನ ನಿಮ್ಮ ಆಸಕ್ತಿಗೆ ನಾವು ನಿಜವಾಗಿಯೂ ಕೃತಜ್ಞರು, '
            'ಮತ್ತು ನಿಮ್ಮ ವ್ಯಾಪಾರಕ್ಕೆ ಶುಭ ಹಾರೈಕೆಗಳು.'}

HOLD0 = {'English': 'Dear Valued Merchant, thank you for applying to Razorpay. Your application is currently under review, and we have not forgotten about you. No '
            'action is needed from you at this time.',
 'Hinglish': 'Dear Valued Merchant, Razorpay mein apply karne ke liye dhanyavaad. Aapki application abhi review mein hai, aur hum aapko bhoole nahi hain. Abhi '
             'aapko koi action lene ki zaroorat nahi hai.',
 'Hindi': 'आदरणीय व्यापारी, Razorpay में आवेदन करने के लिए धन्यवाद। आपका आवेदन अभी समीक्षा में है, और हम आपको भूले नहीं हैं। अभी आपको कोई कार्रवाई करने की '
          'ज़रूरत नहीं है।',
 'Marathi': 'आदरणीय व्यापारी, Razorpay मध्ये अर्ज केल्याबद्दल धन्यवाद. तुमचा अर्ज सध्या पुनरावलोकनाखाली आहे, आणि आम्ही तुम्हाला विसरलेलो नाही. सध्या तुम्हाला '
            'कोणतीही कृती करण्याची गरज नाही.',
 'Tamil': 'மதிப்பிற்குரிய வணிகரே, Razorpay-ல் விண்ணப்பித்ததற்கு நன்றி. உங்கள் விண்ணப்பம் தற்போது மதிப்பாய்வில் உள்ளது, உங்களை நாங்கள் மறக்கவில்லை. இப்போது '
          'நீங்கள் எதுவும் செய்ய வேண்டியதில்லை.',
 'Kannada': 'ಗೌರವಾನ್ವಿತ ವ್ಯಾಪಾರಿಗಳೇ, Razorpay ಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿದ್ದಕ್ಕೆ ಧನ್ಯವಾದಗಳು. ನಿಮ್ಮ ಅರ್ಜಿ ಪ್ರಸ್ತುತ ಪರಿಶೀಲನೆಯಲ್ಲಿದೆ, ಮತ್ತು ನಾವು ನಿಮ್ಮನ್ನು ಮರೆತಿಲ್ಲ. ಈ '
            'ಸಮಯದಲ್ಲಿ ನೀವು ಯಾವುದೇ ಕ್ರಮ ತೆಗೆದುಕೊಳ್ಳುವ ಅಗತ್ಯವಿಲ್ಲ.'}

HOLD7 = {'English': 'Dear Valued Merchant, thank you for your patience. Your Razorpay application is still under review. No action is needed from you at this time.',
 'Hinglish': 'Dear Valued Merchant, aapke sabr ke liye dhanyavaad. Aapki Razorpay application abhi bhi review mein hai. Abhi aapko koi action lene ki zaroorat '
             'nahi hai.',
 'Hindi': 'आदरणीय व्यापारी, आपके धैर्य के लिए धन्यवाद। आपका Razorpay आवेदन अभी भी समीक्षा में है। अभी आपको कोई कार्रवाई करने की ज़रूरत नहीं है।',
 'Marathi': 'आदरणीय व्यापारी, तुमच्या संयमाबद्दल धन्यवाद. तुमचा Razorpay अर्ज अजूनही पुनरावलोकनाखाली आहे. सध्या तुम्हाला कोणतीही कृती करण्याची गरज नाही.',
 'Tamil': 'மதிப்பிற்குரிய வணிகரே, உங்கள் பொறுமைக்கு நன்றி. உங்கள் Razorpay விண்ணப்பம் இன்னும் மதிப்பாய்வில் உள்ளது. இப்போது நீங்கள் எதுவும் செய்ய '
          'வேண்டியதில்லை.',
 'Kannada': 'ಗೌರವಾನ್ವಿತ ವ್ಯಾಪಾರಿಗಳೇ, ನಿಮ್ಮ ತಾಳ್ಮೆಗೆ ಧನ್ಯವಾದಗಳು. ನಿಮ್ಮ Razorpay ಅರ್ಜಿ ಇನ್ನೂ ಪರಿಶೀಲನೆಯಲ್ಲಿದೆ. ಈ ಸಮಯದಲ್ಲಿ ನೀವು ಯಾವುದೇ ಕ್ರಮ ತೆಗೆದುಕೊಳ್ಳುವ '
            'ಅಗತ್ಯವಿಲ್ಲ.'}

STEPNAME = {'English': {'Business details': 'Business details',
             'KYC docs': 'KYC documents',
             'Bank verification': 'Bank verification',
             'Website/App review': 'Website/App review'},
 'Hinglish': {'Business details': 'Business details',
              'KYC docs': 'KYC documents',
              'Bank verification': 'Bank verification',
              'Website/App review': 'Website/App review'},
 'Hindi': {'Business details': 'बिज़नेस जानकारी', 'KYC docs': 'KYC दस्तावेज़', 'Bank verification': 'बैंक सत्यापन', 'Website/App review': 'वेबसाइट/ऐप समीक्षा'},
 'Marathi': {'Business details': 'व्यवसाय माहिती',
             'KYC docs': 'KYC कागदपत्रे',
             'Bank verification': 'बँक पडताळणी',
             'Website/App review': 'वेबसाइट/अॅप पुनरावलोकन'},
 'Tamil': {'Business details': 'வணிக விவரங்கள்',
           'KYC docs': 'KYC ஆவணங்கள்',
           'Bank verification': 'வங்கி சரிபார்ப்பு',
           'Website/App review': 'இணையதளம்/செயலி மதிப்பாய்வு'},
 'Kannada': {'Business details': 'ವ್ಯಾಪಾರ ವಿವರಗಳು',
             'KYC docs': 'KYC ದಾಖಲೆಗಳು',
             'Bank verification': 'ಬ್ಯಾಂಕ್ ಪರಿಶೀಲನೆ',
             'Website/App review': 'ವೆಬ್\u200cಸೈಟ್/ಆ್ಯಪ್ ಪರಿಶೀಲನೆ'}}

STEP_OF = {'R01': 'KYC docs',
 'R02': 'KYC docs',
 'R03': 'Bank verification',
 'R04': 'Bank verification',
 'R05': 'KYC docs',
 'R06': 'Website/App review',
 'R07': 'Website/App review',
 'R08': 'KYC docs',
 'R09': 'KYC docs',
 'R11': 'Website/App review'}


def _step(lang, step):
    return STEPNAME[lang][step]


def day0(code, lang, tone='reminder', channel='WhatsApp', stuck=False, step=None):
    prob, fix = BODY[code][lang]
    if code == 'R13':
        sname = _step(lang, step)
        prob = prob.format(step=sname)
        head = HEAD['r13soft'][lang] if tone == 'soft' else HEAD[tone][lang]
        parts = [head]
        why = WHY_R13[lang]
    else:
        sname = _step(lang, STEP_OF[code])
        head = HEAD[tone][lang]
        parts = [head, STEP_LINE[lang].format(step=sname)]
        why = WHY[lang]
    if stuck:
        parts.append(EMPATHY[lang])
    parts += [prob, fix, why]
    body = GREET[lang] + '\n' + ' '.join(parts) + '\n' + CTA[lang] + '\n' + HELP[lang]
    body += ('\n' + SIGN[lang]) if channel == 'Email' else ('\n' + STOP[lang])
    return body


def day3(code, lang, step=None):
    if code == 'R13':
        return GREET[lang] + ' ' + D3_R13[lang].format(step=_step(lang, step))
    return GREET[lang] + ' ' + D3[lang].format(s=SHORT[code][lang])


def day7(code, lang, step=None):
    if code == 'R13':
        s = ('the ' if lang == 'English' else '') + _step(lang, step) + ' ' + STEPWORD[lang]
    else:
        s = SHORT[code][lang]
    return GREET[lang] + ' ' + D7[lang].format(s=s)


def wrap(msg, lang, channel):
    return msg + '\n' + (STOP[lang] if channel == 'WhatsApp' else SIGN[lang])


# ====================================================================================
# v2 FORMAT (approved 7 Nov): thank-you opener, steps-left line, "We noticed" problem line,
# bullet fixes, quoted HELP and STOP replies, no emoji, merchant name with fallback.
# Problem and fix FACTS are unchanged from the approved library above. Regional wording was
# reviewed and approved by native speakers.
# ====================================================================================
import re

ORDER = ['Business details', 'KYC docs', 'Bank verification', 'Website/App review']
CHOOSE_ONE = ('R01', 'R02', 'R03', 'R11')
NOTICE = ('R01', 'R03', 'R06', 'R08', 'R09', 'R11')
SPLIT = re.compile(r'(?<=[.।])\s+')

OPEN_SOFT = {'English': 'Thank you for trusting us and starting your setup with Razorpay.',
 'Hinglish': 'Hum par bharosa karke Razorpay ke saath application shuru karne ke liye dhanyavaad.',
 'Hindi': 'हम पर भरोसा करके Razorpay के साथ अपना आवेदन शुरू करने के लिए धन्यवाद।',
 'Marathi': 'आमच्यावर विश्वास ठेवून Razorpay सोबत तुमचा अर्ज सुरू केल्याबद्दल धन्यवाद.',
 'Tamil': 'எங்களை நம்பி Razorpay உடன் உங்கள் விண்ணப்பத்தைத் தொடங்கியதற்கு நன்றி.',
 'Kannada': 'ನಮ್ಮ ಮೇಲೆ ನಂಬಿಕೆ ಇಟ್ಟು Razorpay ಜೊತೆ ನಿಮ್ಮ ಅರ್ಜಿ ಆರಂಭಿಸಿದ್ದಕ್ಕೆ ಧನ್ಯವಾದಗಳು.'}
OPEN_TONE = {'soft': OPEN_SOFT,
 'reminder': dict(HEAD['reminder'], English='Your Razorpay setup is still waiting for you.'),
 'gentle': dict(HEAD['gentle'], English='We are here whenever you are ready to finish your Razorpay setup.')}

# steps left: index 0 = one step left ... index 3 = four left ("a few")
STEPS = {'English': ['You are just one step away from completing it.', 'You are just two steps away from completing it.',
                     'You are just three steps away from completing it.', 'You are just a few steps away from completing it.'],
 'Hinglish': ['Aap application poori karne se bas ek step door hain.', 'Aap application poori karne se bas do steps door hain.',
              'Aap application poori karne se bas teen steps door hain.', 'Aap application poori karne se bas kuch steps door hain.'],
 'Hindi': ['आप आवेदन पूरा करने से बस एक कदम दूर हैं।', 'आप आवेदन पूरा करने से बस दो कदम दूर हैं।',
           'आप आवेदन पूरा करने से बस तीन कदम दूर हैं।', 'आप आवेदन पूरा करने से बस कुछ ही कदम दूर हैं।'],
 'Marathi': ['तुम्ही अर्ज पूर्ण करण्यापासून फक्त एक पाऊल दूर आहात.', 'तुम्ही अर्ज पूर्ण करण्यापासून फक्त दोन पावले दूर आहात.',
             'तुम्ही अर्ज पूर्ण करण्यापासून फक्त तीन पावले दूर आहात.', 'तुम्ही अर्ज पूर्ण करण्यापासून फक्त काही पावले दूर आहात.'],
 'Tamil': ['உங்கள் விண்ணப்பத்தை முடிக்க இன்னும் ஒரு படி மட்டுமே உள்ளது.', 'உங்கள் விண்ணப்பத்தை முடிக்க இன்னும் இரண்டு படிகள் மட்டுமே உள்ளன.',
           'உங்கள் விண்ணப்பத்தை முடிக்க இன்னும் மூன்று படிகள் மட்டுமே உள்ளன.', 'உங்கள் விண்ணப்பத்தை முடிக்க இன்னும் சில படிகள் மட்டுமே உள்ளன.'],
 'Kannada': ['ನಿಮ್ಮ ಅರ್ಜಿ ಪೂರ್ಣಗೊಳಿಸಲು ಇನ್ನು ಕೇವಲ ಒಂದು ಹಂತ ಬಾಕಿ ಇದೆ.', 'ನಿಮ್ಮ ಅರ್ಜಿ ಪೂರ್ಣಗೊಳಿಸಲು ಇನ್ನು ಕೇವಲ ಎರಡು ಹಂತಗಳು ಬಾಕಿ ಇವೆ.',
             'ನಿಮ್ಮ ಅರ್ಜಿ ಪೂರ್ಣಗೊಳಿಸಲು ಇನ್ನು ಕೇವಲ ಮೂರು ಹಂತಗಳು ಬಾಕಿ ಇವೆ.', 'ನಿಮ್ಮ ಅರ್ಜಿ ಪೂರ್ಣಗೊಳಿಸಲು ಇನ್ನು ಕೆಲವು ಹಂತಗಳು ಬಾಕಿ ಇವೆ.']}
STEPS7_EN = [s.replace('completing it', 'completing your Razorpay setup') for s in STEPS['English']]

def steps_line(lang, step, d7=False):
    n = len(ORDER) - ORDER.index(step)
    return (STEPS7_EN if (d7 and lang == 'English') else STEPS[lang])[n - 1]

FIX_LABEL = {'choose': {'English': "Here's how you can fix it (choose one):", 'Hinglish': 'Aap ise aise theek kar sakte hain (koi ek chunein):',
  'Hindi': 'आप इसे इस तरह ठीक कर सकते हैं (कोई एक चुनें):', 'Marathi': 'तुम्ही हे असे दुरुस्त करू शकता (कोणताही एक निवडा):',
  'Tamil': 'இதை இப்படிச் சரிசெய்யலாம் (ஏதாவது ஒன்றைத் தேர்ந்தெடுக்கவும்):', 'Kannada': 'ಇದನ್ನು ಹೀಗೆ ಸರಿಪಡಿಸಬಹುದು (ಯಾವುದಾದರೂ ಒಂದನ್ನು ಆಯ್ಕೆಮಾಡಿ):'},
 'do': {'English': "Here's how you can fix it:", 'Hinglish': 'Aap ise aise theek kar sakte hain:', 'Hindi': 'आप इसे इस तरह ठीक कर सकते हैं:',
  'Marathi': 'तुम्ही हे असे दुरुस्त करू शकता:', 'Tamil': 'இதை இப்படிச் சரிசெய்யலாம்:', 'Kannada': 'ಇದನ್ನು ಹೀಗೆ ಸರಿಪಡಿಸಬಹುದು:'},
 'r13': {'English': 'Here are your next steps:', 'Hinglish': 'Aapke agle steps:', 'Hindi': 'आपके अगले कदम:',
  'Marathi': 'तुमची पुढील पावले:', 'Tamil': 'உங்கள் அடுத்த படிகள்:', 'Kannada': 'ನಿಮ್ಮ ಮುಂದಿನ ಹಂತಗಳು:'}}

R13_NOTICE = {'English': 'We noticed you paused at the {step} step.', 'Hinglish': 'Humne dekha ki aap {step} step par ruk gaye.',
 'Hindi': 'हमने देखा कि आप {step} चरण पर रुक गए।', 'Marathi': 'आमच्या लक्षात आले की तुम्ही {step} टप्प्यावर थांबलात.',
 'Tamil': 'நீங்கள் {step} படியில் நின்றுவிட்டீர்கள் என்பதை நாங்கள் கவனித்தோம்.', 'Kannada': 'ನೀವು {step} ಹಂತದಲ್ಲಿ ನಿಲ್ಲಿಸಿದ್ದೀರಿ ಎಂದು ನಾವು ಗಮನಿಸಿದ್ದೇವೆ.'}
R13_BULLETS = {'English': ['Open the link below', 'Continue from the {step} step'],
 'Hinglish': ['Neeche diya link kholein', '{step} step se aage badhein'], 'Hindi': ['नीचे दिया लिंक खोलें', '{step} चरण से आगे बढ़ें'],
 'Marathi': ['खालील लिंक उघडा', '{step} टप्प्यापासून पुढे जा'], 'Tamil': ['கீழே உள்ள இணைப்பைத் திறக்கவும்', '{step} படியிலிருந்து தொடரவும்'],
 'Kannada': ['ಕೆಳಗಿನ ಲಿಂಕ್ ತೆರೆಯಿರಿ', '{step} ಹಂತದಿಂದ ಮುಂದುವರಿಸಿ']}

HELP_W = {'English': 'For assistance, reply "HELP" to this message. Our team will be happy to help you.',
 'Hinglish': 'Madad ke liye is message ka reply "HELP" likhkar karein. Hamari team khushi se aapki madad karegi.',
 'Hindi': 'सहायता के लिए इस संदेश के जवाब में "HELP" लिखें। हमारी टीम खुशी से आपकी मदद करेगी।',
 'Marathi': 'मदतीसाठी या संदेशाला "HELP" असे उत्तर द्या. आमची टीम आनंदाने तुमची मदत करेल.',
 'Tamil': 'உதவிக்கு, இந்தச் செய்திக்கு "HELP" என்று பதிலளிக்கவும். எங்கள் குழு மகிழ்ச்சியுடன் உங்களுக்கு உதவும்.',
 'Kannada': 'ಸಹಾಯಕ್ಕಾಗಿ ಈ ಸಂದೇಶಕ್ಕೆ "HELP" ಎಂದು ಉತ್ತರಿಸಿ. ನಮ್ಮ ತಂಡ ಸಂತೋಷದಿಂದ ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ.'}
HELP_E = {'English': 'For assistance, reply to this email. Our team will be happy to help you.',
 'Hinglish': 'Madad ke liye is email ka reply karein. Hamari team khushi se aapki madad karegi.',
 'Hindi': 'सहायता के लिए इस ईमेल का जवाब दें। हमारी टीम खुशी से आपकी मदद करेगी।',
 'Marathi': 'मदतीसाठी या ईमेलला उत्तर द्या. आमची टीम आनंदाने तुमची मदत करेल.',
 'Tamil': 'உதவிக்கு, இந்த மின்னஞ்சலுக்குப் பதிலளிக்கவும். எங்கள் குழு மகிழ்ச்சியுடன் உங்களுக்கு உதவும்.',
 'Kannada': 'ಸಹಾಯಕ್ಕಾಗಿ ಈ ಇಮೇಲ್‌ಗೆ ಉತ್ತರಿಸಿ. ನಮ್ಮ ತಂಡ ಸಂತೋಷದಿಂದ ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ.'}
HELP = HELP_W
STOP = {'English': 'Reply "STOP" to stop these messages.', 'Hinglish': 'In messages ko rokne ke liye "STOP" likhkar reply karein.',
 'Hindi': 'इन संदेशों को रोकने के लिए "STOP" लिखकर जवाब दें।', 'Marathi': 'हे संदेश थांबवण्यासाठी "STOP" असे उत्तर द्या.',
 'Tamil': 'இந்தச் செய்திகளை நிறுத்த "STOP" என்று பதிலளிக்கவும்.', 'Kannada': 'ಈ ಸಂದೇಶಗಳನ್ನು ನಿಲ್ಲಿಸಲು "STOP" ಎಂದು ಉತ್ತರಿಸಿ.'}
WHY['English'] = 'This is needed before you can start accepting payments.'
WHY_R13['English'] = 'Finishing your setup is needed before you can start accepting payments.'
SUBJ['day0']['English'] = 'Your Razorpay setup: here is how to continue'
SUBJ['day3']['English'] = 'A reminder about your Razorpay setup'
SUBJ['day7']['English'] = 'Need help with your Razorpay setup?'

# English problem line, bold clause and bullets (approved wording)
EN = {
 'R01': ('We noticed that *the name on your PAN card does not match the business name in your application.*', ['*Upload the PAN of the business* (or of the owner, for a proprietorship) that matches your application', '*Or correct the business name* in your application to match your PAN']),
 'R02': ('We could not validate your GST details. *The GSTIN may be wrong, inactive, or linked to a different legal name or address.*', ['*Enter the correct GSTIN*', '*Or upload a current GST certificate* that matches your legal name and address']),
 'R03': ('We noticed that *the name on your bank account does not match your business or PAN name.*', ["*Use a current account in the business name* (the owner's name for a proprietorship)", '*Or upload a bank letter or cancelled cheque* that shows the matching name']),
 'R04': ('We could not verify your bank account with the small test credit.', ['*Re-enter the account number and IFSC* carefully', '*Check that the account is active* and can receive credits']),
 'R05': ('We could not read your document. *It may be blurred, cropped or password-protected.*', ['*Upload a clear, full-page colour scan*', 'Use a PDF, JPG or PNG file under 5 MB']),
 'R06': ('We noticed that *your website or app is missing some required pages.*', ['*Add these pages with working links:* Terms & Conditions, Privacy Policy, Refund/Cancellation Policy and Contact details', 'Then submit your website link again']),
 'R07': ('We could not review your website. *It is not live, or it needs a login to see products and prices.*', ['*Make the website open to everyone,* with products, prices and contact details visible', 'Then submit it again']),
 'R08': ('We noticed that *your address proof is missing, out of date, or shows a different address from your application.*', ['*Upload a recent utility bill, rent agreement or other valid address proof*', 'Make sure it matches the address in your application']),
 'R09': ('We noticed that *the ID of your authorised signatory or director is missing, or its details do not match your application.*', ['*Upload a valid ID of the authorised signatory*', 'Make sure the name and date of birth match your application']),
 'R11': ('We noticed that *the business category you selected is different from what your website sells.*', ['*Select the correct category*', '*Or share a short note with evidence* explaining your business model, for a second review']),
}
SHORT_D7_EN = {'R05': 'uploading a clearer document'}

NOTICE_FMT = {'Hinglish': lambda s: 'Humne dekha ki ' + s[0].lower() + s[1:],
 'Hindi': lambda s: 'हमने देखा कि ' + s, 'Marathi': lambda s: 'आमच्या लक्षात आले की ' + s,
 'Tamil': lambda s: s.rstrip('.') + ' என்பதை நாங்கள் கவனித்தோம்.', 'Kannada': lambda s: s.rstrip('.') + ' ಎಂದು ನಾವು ಗಮನಿಸಿದ್ದೇವೆ.'}
GREET_NAME = {'English': 'Dear {n},', 'Hinglish': 'Dear {n},', 'Hindi': 'आदरणीय {n},', 'Marathi': 'आदरणीय {n},',
              'Tamil': 'மதிப்பிற்குரிய {n},', 'Kannada': 'ಗೌರವಾನ್ವಿತ {n},'}
_BAD_NAME = ['guarantee', 'approved', 'approval', 'within', 'today', 'tomorrow', 'refund', 'waive', 'sanction', 'screening',
             'compliance', 'risk', 'restricted', 'reject', 'blacklist', 'bypass']

def greeting(lang, name=None):
    """Merchant name if one exists and is safe, otherwise the standard greeting."""
    if isinstance(name, str):
        n = name.strip()
        if 0 < len(n) <= 60 and not any(ch.isdigit() for ch in n) and not any(w in n.lower() for w in _BAD_NAME):
            return GREET_NAME[lang].format(n=n)
    return GREET[lang]

def personalise(text, lang, name):
    g = greeting(lang, name)
    return text.replace(GREET[lang], g, 1) if g != GREET[lang] else text

def _bold(s): return '*' + s + '*'
def _email(text): return re.sub(r'\*(.+?)\*', r'**\1**', text)

def _problem_and_bullets(code, lang, step):
    if code == 'R13':
        sn = _step(lang, step)
        lead = R13_NOTICE[lang].format(step=sn)
        lead = _bold(lead) if lang != 'English' else lead.replace('the %s step.' % sn, '*the %s step.*' % sn)
        return lead, FIX_LABEL['r13'][lang], [b.format(step=sn) for b in R13_BULLETS[lang]]
    label = FIX_LABEL['choose' if code in CHOOSE_ONE else 'do'][lang]
    if lang == 'English':
        lead, bullets = EN[code]
        return lead, label, bullets
    prob, fix = BODY[code][lang]
    sents = SPLIT.split(prob.strip())
    if code in NOTICE:
        sents = [NOTICE_FMT[lang](sents[0])] + sents[1:]
    lead = _bold(' '.join(sents))
    bullets = [b.strip().rstrip('.।') for b in SPLIT.split(fix.strip()) if b.strip()]
    return lead, label, bullets

def day0(code, lang, tone='reminder', channel='WhatsApp', stuck=False, step=None, name=None):
    step_for_count = step if code == 'R13' else STEP_OF[code]
    lead, label, bullets = _problem_and_bullets(code, lang, step)
    parts = [greeting(lang, name), OPEN_TONE[tone][lang] + ' ' + steps_line(lang, step_for_count)]
    if stuck:
        parts.append(EMPATHY[lang])
    parts += [lead, label + '\n' + '\n'.join('• ' + b for b in bullets), WHY_R13[lang] if code == 'R13' else WHY[lang],
              CTA[lang], HELP_W[lang] if channel == 'WhatsApp' else HELP_E[lang],
              STOP[lang] if channel == 'WhatsApp' else SIGN[lang]]
    text = '\n\n'.join(parts)
    return _email(text) if channel == 'Email' else text

def _strip_cta(text):
    return re.sub(r'\s*[^.।]*\[resume link\]\s*$', '', text).strip()

def day3(code, lang, step=None, name=None):
    st = step if code == 'R13' else STEP_OF[code]
    if lang == 'English':
        body = ('A reminder from Razorpay: your setup is waiting for you at the %s step.' % _step(lang, step)) if code == 'R13' \
            else 'A reminder from Razorpay: your setup is still waiting on %s.' % SHORT[code][lang]
    else:
        raw = D3_R13[lang].format(step=_step(lang, step)) if code == 'R13' else D3[lang].format(s=SHORT[code][lang])
        body = _strip_cta(raw); body = body[0].upper() + body[1:]
    return '\n\n'.join([greeting(lang, name), body + ' ' + steps_line(lang, st), CTA[lang]])

def day7(code, lang, step=None, name=None):
    st = step if code == 'R13' else STEP_OF[code]
    if lang == 'English':
        s = ('the %s step' % _step(lang, step)) if code == 'R13' else SHORT_D7_EN.get(code, SHORT[code][lang])
        q = 'Do you need help with %s?' % s
    else:
        s = (_step(lang, step) + ' ' + STEPWORD[lang]) if code == 'R13' else SHORT[code][lang]
        q = D7[lang].format(s=s).split('?')[0] + '?'
        q = q[0].upper() + q[1:]
    return '\n\n'.join([greeting(lang, name), q + ' ' + steps_line(lang, st, d7=True), CTA[lang]])

def wrap(msg, lang, channel):
    out = msg + '\n\n' + (HELP_W[lang] if channel == 'WhatsApp' else HELP_E[lang]) + '\n\n' + (STOP[lang] if channel == 'WhatsApp' else SIGN[lang])
    return _email(out) if channel == 'Email' else out
