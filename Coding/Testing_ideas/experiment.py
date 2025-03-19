import random as rnd

class creature():
    creatures=[]
    def __init__(self, 
                name, 
                hp=None, 
                max_hp=None, 
                attacks=None,
                actions=None
                ) -> None:
        self.name=name
        self.hp=hp
        self.max_hp=max_hp
        if attacks==None:
            attacks={}
        self.attacks=attacks
        if actions==None:
            actions={}
        self.actions=actions
        creature.creatures.append(self)
    
def attack(attacker, target, attack_name):
    attack_stat=attacker.attacks[attack_name]["attack_stat"]
    attack_damage=attacker.attacks[attack_name]["damage_dice"]
    n_dice, dice_type=parse_dice(attack_damage)
    attack_damage_type=attacker.attacks[attack_name]["damage_type"]
    attack_stat_mod=attacker.get_stat_modifier(attack_stat)
    roll_result=basic_roll(attack_stat_mod,"adv")
    print(f"{attacker.name} rolled a {roll_result}")
    crit=crit_check(roll_result,attack_stat_mod)
    target_ac=target.ac
    if crit=="success":
        print("I got a critical hit")
        n_dice, dice_type= parse_dice(attack_damage)
        damage=n_dice*dice_type
        damage+=dmg_roll(n_dice, dice_type, attack_stat_mod)
        target.take_damage(damage, type=attack_damage_type)
    elif crit=="failure":
        print("I got as critical miss")
    elif roll_result>=target_ac:
        print(f"that hits {target.name}")
        target.take_damage(dmg_roll(n_dice, dice_type, attack_stat_mod), type=attack_damage_type, multiplier=1)
    else:
        print(f"that does not hit {target.name}")

    def roll_hp(self):
            result=rnd.randint(10,50)
            self.hp=result
            self.max_hp=result

    def take_damage(self, amount):
        amount=int(amount)
        if self.hp-amount<=self.max_hp:
            self.hp-=amount
        elif amount<0:
            self.hp=self.max_hp
        if amount>0:
            print(f"{self.name} has taken {amount} point(s) of {type} damage")
            if self.hp<=0:
                print(f"{self.name} has died")
            else:
                print(f"{self.name}'s remaining hp is {self.hp}")
        elif amount==0:
            print(f"{self.name} is immune to {type} damage")
        else:
            print(f"{self.name} has healed {amount*(-1)} point(s) of damage")
            print(f"{self.name}'s remaining hp is {self.hp}")

#class Category():
#    
#    def __init__(self, name ledger=None)) -> None:
#        self.name=name
#        if ledger == None:
#            ledger=[]
#        self.ledger=ledger
#        self.total=0
#    
#    def deposit(amount, description=None):
#
#
#def create_spend_chart(categories):
#def convert_to_srt(entries):
#    srt_lines = []
#    for index, entry in enumerate(entries, start=1):
#        start_time = entry['start']
#        end_time = start_time + entry['duration']
#
#        srt_start_time = format_time(start_time)
#        srt_end_time = format_time(end_time)
#
#        text = entry['text']
#
#        srt_lines.append(f"{index}\n{srt_start_time} --> {srt_end_time}\n{text}\n")
#
#    return '\n'.join(srt_lines)
#
#
#def format_time(seconds):
#    milliseconds = int((seconds - int(seconds)) * 1000)
#    time_obj = time.gmtime(seconds)
#    formatted_time = time.strftime("%H:%M:%S,", time_obj)
#    return f"{formatted_time}{milliseconds:03}"
#
#
#if __name__ == "__main__":
#    import time
#
#    # Sample dictionary entries
#    entries = [
#            {'text': 'انت اكثر وحدة بتعرفي ظروفي', 'start': 3.469, 'duration': 2.0},
#            {'text': 'بليز ما تخذليني ،انا محتاجيتك اليوم', 'start': 6.25, 'duration': 3.035},
#            {'text': 'يلا لفي، بليز لفي', 'start': 9.685, 'duration': 2.315},
#            {'text': 'يس اشتغلت اشتغلت', 'start': 13.09, 'duration': 2.345},
#            {'text': 'يا ساتر شو في', 'start': 15.889, 'duration': 1.382},
#            {'text': 'سند افتح الباب ماما', 'start': 17.434, 'duration': 2.0},
#            {'text': 'هاي آنتي', 'start': 20.796, 'duration': 0.946},
#            {'text': 'ماما ام انصاف عالباب', 'start': 22.069, 'duration': 2.218},
#            {'text': 'اهلا ام انصاف كيفك؟', 'start': 24.487, 'duration': 2.418},
#            {'text': 'منيحة منيحة حبيبتي', 'start': 27.177, 'duration': 1.201},
#            {'text': 'بس مستعجلة كتير كتير', 'start': 28.378, 'duration': 1.855},
#            {'text': 'خير، في اشي', 'start': 30.415, 'duration': 1.305},
#            {'text': 'في اكيد في', 'start': 31.829, 'duration': 1.171},
#            {'text': 'في عنا جار جديد في العمارة اللي جمبنا', 'start': 33.163, 'duration': 2.945},
#            {'text': 'بده يتعرف على الجيران وعازم الكل على قهوة المسا', 'start': 36.235, 'duration': 2.636},
#            {'text': 'ما تنسي تخبري أبو سند', 'start': 39.0, 'duration': 1.583},
#            {'text': 'مين هذا وشو عرفك فيه ؟', 'start': 40.88, 'duration': 2.472},
#            {'text': 'شفته بنزل اغراضه وسـألني عن رقم الحارس وطلب مني اعزم عمارتنا اليوم على ٦', 'start': 43.56, 'duration': 5.796},
#            {'text': 'بس مبين عليه مرتب ومنصب عالي وكتير راقي', 'start': 49.556, 'duration': 4.844},
#            {'text': 'يا سلام، وكيف عرفتي يعني ؟ ', 'start': 54.4, 'duration': 2.28},
#            {'text': 'عيب', 'start': 56.68, 'duration': 0.747},
#            {'text': 'انا الواحد بس يقولي مرحبا بكون عملت فحص وبطلع تقرير كامل عنه', 'start': 57.808, 'duration': 5.506},
#            {'text': 'يلا انا لازم اروح اخبر العمارة', 'start': 63.514, 'duration': 2.381},
#            {'text': 'خبري ابو سند بنشوفكم اليوم على ال ٦', 'start': 66.077, 'duration': 2.49},
#            {'text': 'باي', 'start': 68.567, 'duration': 0.993},
#            {'text': 'باي', 'start': 69.705, 'duration': 0.656},
#            {'text': 'انت متأكدة من هالقصة ', 'start': 72.0, 'duration': 1.491},
#            {'text': 'هيك حكت ام انصاف', 'start': 73.582, 'duration': 1.328},
#            {'text': 'هلا على كل حال بنشوف ', 'start': 75.0, 'duration': 1.473},
#            {'text': 'ييي بابا مش هذا خلدون صاحبك', 'start': 78.473, 'duration': 2.708},
#            {'text': 'اشوف', 'start': 81.399, 'duration': 0.728},
#            {'text': 'ايه هو بذاته', 'start': 82.436, 'duration': 1.564},
#            {'text': 'هذا هو الجار الجديد ؟', 'start': 84.454, 'duration': 1.782},
#            {'text': 'يا فرحتنا فيه', 'start': 87.0, 'duration': 1.528},
#            {'text': 'تأخرتوا', 'start': 88.728, 'duration': 0.783},
#            {'text': 'هيو، الواقف هناك شفتيه', 'start': 89.511, 'duration': 2.163},
#            {'text': 'اه بعرفه', 'start': 91.783, 'duration': 0.91},
#            {'text': 'هذا خلدون صاحب ابو سند', 'start': 93.0, 'duration': 1.728},
#            {'text': 'قصدي كان بصف ابو سند', 'start': 94.728, 'duration': 2.091},
#            {'text': 'جديد صار مدير شركة كبيرة', 'start': 97.001, 'duration': 2.0},
#            {'text': 'يا جماعة انا محظوظ اني اكون جار الكم وحبيت اتعرف عليكم واحد واحد', 'start': 100.581, 'duration': 6.396},
#            {'text': ' مبارح رجعت من فرنسا وانا قاعد في الشونزاليزيه بحتسي القهوة الصباحية', 'start': 107.377, 'duration': 7.158},
#            {'text': 'وباكل الكروسون اتمنيتكم تكونوا معي وجبتلكم حصتكم', 'start': 114.662, 'duration': 5.687},
#            {'text': 'تفضلوا', 'start': 120.749, 'duration': 0.674},
#            {'text': '( بالفرنسي)', 'start': 122.004, 'duration': 2.581},
#            {'text': 'مش قلتلك شكله واصل', 'start': 125.021, 'duration': 1.691},
#            {'text': '( بالفرنسي)', 'start': 126.966, 'duration': 4.034},
#            {'text': 'سند بس ماما', 'start': 131.254, 'duration': 1.473},
#            {'text': 'لما كنت بحتسي القهوة في شارع الشانزاليزيه', 'start': 133.999, 'duration': 4.001},
#            {'text': 'يعني مش فيها شوية عرط ولا كيف ؟', 'start': 138.127, 'duration': 2.963},
#            {'text': 'انت بس زعلان لانه ما اتذكرك اخر مرة', 'start': 141.926, 'duration': 3.199},
#            {'text': 'ابدا', 'start': 145.125, 'duration': 0.822},
#            {'text': 'وبعدين قهوة ابو العبد ازكى من قهوته', 'start': 146.474, 'duration': 3.072},
#            {'text': 'بس بابا الكرواسون بشهي', 'start': 149.709, 'duration': 2.345},
#            {'text': 'انا اكلت ٤', 'start': 152.054, 'duration': 1.292},
#            {'text': 'انا ما ذقته', 'start': 153.437, 'duration': 0.946},
#            {'text': 'نفسي لاعية من الحلو', 'start': 154.873, 'duration': 2.0},
#            {'text': 'تفضلوا قدامي', 'start': 157.2, 'duration': 1.019},
#            {'text': 'مش معقول', 'start': 163.596, 'duration': 1.264},
#            {'text': 'هذا المشهد مهم ومصيري', 'start': 165.078, 'duration': 1.962},
#            {'text': 'الف مرة قلتلكم بدنا تلفزيون جديد', 'start': 167.149, 'duration': 2.454},
#            {'text': 'انا عندي الحل', 'start': 169.766, 'duration': 0.856},
#            {'text': 'طولوا بالكم', 'start': 170.92, 'duration': 0.856},
#            {'text': 'اشتغل اشتغل', 'start': 176.807, 'duration': 0.873},
#            {'text': 'ماما علي الصوت شوي', 'start': 177.68, 'duration': 1.51},
#            {'text': 'خلص هيك منيح بلاش يخرب', 'start': 179.353, 'duration': 2.218},
#            {'text': 'يزن شوف مين على الباب', 'start': 182.48, 'duration': 1.8},
#            {'text': 'بابا بابا هذه الك', 'start': 186.387, 'duration': 1.546},
#            {'text': 'بوفيه مشاوي مفتوح للجيران الاكارم حلوان صفقة كبيرة تم توقيعها لصالح شركتي', 'start': 189.077, 'duration': 6.287},
#            {'text': 'مع خالص تحياتي، جاركم خلدون', 'start': 195.364, 'duration': 2.49},
#            {'text': 'أيه! هذا جارنا الجديد', 'start': 198.308, 'duration': 2.0},
#            {'text': 'يسعده وما يبعده', 'start': 202.111, 'duration': 1.382},
#            {'text': 'شو هالجار المرتب المتكتك', 'start': 203.493, 'duration': 2.0},
#            {'text': 'اي هيك الحكي ولا بلاش', 'start': 206.892, 'duration': 1.764},
#            {'text': 'كله حكي ومواعظ احنا بدنا أفعال', 'start': 208.801, 'duration': 3.453},
#            {'text': 'واخيرا رح نوكل مشاوي', 'start': 214.161, 'duration': 2.926},
#            {'text': 'معقول انا ظالمه لهزلمة', 'start': 217.378, 'duration': 1.622},
#            {'text': 'شو هذا الصوت ؟', 'start': 219.16, 'duration': 1.11},
#            {'text': 'شو مالكم خايفين هذه الغسالة عم تعصر', 'start': 220.651, 'duration': 2.909},
#            {'text': 'بابا اظن صار بدنا غسالة جديدة', 'start': 223.923, 'duration': 2.2},
#            {'text': 'ولا شو ههههه', 'start': 226.123, 'duration': 1.6},
#            {'text': 'شكله الخروف بلدي', 'start': 231.665, 'duration': 2.163},
#            {'text': 'اللحمة مثل الفستق', 'start': 234.0, 'duration': 2.0},
#            {'text': 'يسلمو يا جار', 'start': 236.527, 'duration': 1.055},
#            {'text': 'مش فاهم شو ماله عليك ابو سند', 'start': 237.691, 'duration': 1.582},
#            {'text': 'قال مش جوعان قال', 'start': 239.273, 'duration': 1.11},
#            {'text': 'عادي', 'start': 240.783, 'duration': 0.747},
#            {'text': ' قلت للشباب يخلولوا حصته', 'start': 241.784, 'duration': 2.127},
#            {'text': 'زوق، زوق مستر خلدون', 'start': 244.111, 'duration': 2.599},
#            {'text': 'بدناش نحكي بس الغيرة مرات بتعمل عمايل', 'start': 246.873, 'duration': 3.635},
#            {'text': 'بدي اسألك شغلة، ريحتك اوريجينال مش تركيب اه', 'start': 251.325, 'duration': 5.034},
#            {'text': 'لانه انا كان عندي بزنز روايح وكريمات يعني بفهم بهالشغلات هههه', 'start': 256.504, 'duration': 5.687},
#            {'text': 'الف مبروك جار', 'start': 263.245, 'duration': 1.564},
#            {'text': 'ما قلتلي شو هي الصفقة اللي وقعتها ؟', 'start': 265.336, 'duration': 2.727},
#            {'text': 'واخيرا حدا سألني', 'start': 268.2, 'duration': 1.6},
#            {'text': 'وحابب اخبر الجميع', 'start': 270.181, 'duration': 1.746},
#            {'text': 'اسمعوني يا جماعة', 'start': 272.545, 'duration': 1.364},
#            {'text': 'احنا اتعاقدنا مع شركة المانية بتصنع اجهزة كهربائية حديثة', 'start': 274.163, 'duration': 5.106},
#            {'text': 'وكوسيلة للتسويق', 'start': 279.523, 'duration': 1.637},
#            {'text': 'انتو اهلي وعيلتي اول ناس رح تستفيدوا من هالفرصة', 'start': 281.36, 'duration': 4.18},
#            {'text': 'اي حدا فيكم عنده غسالة او تلاجة او تلفزيون قديمة او زهق منها', 'start': 285.794, 'duration': 5.669},
#            {'text': 'بقدر يستبدلها بجهاز جديدة من شركتنا', 'start': 291.572, 'duration': 2.999},
#            {'text': 'معاكم لبكرا بعد الظهر', 'start': 294.68, 'duration': 1.782},
#            {'text': 'كل واحد بسجل اسمه والجهاز اللي جابه وخلال يومين بتوصلكم الاجهزة الجديدة', 'start': 296.68, 'duration': 6.32},
#            {'text': 'شو .. معقول .. شو بحكي', 'start': 303.24, 'duration': 2.908},
#            {'text': 'وأخيرا رح نبدل التلفزيون تبعنا ', 'start': 307.184, 'duration': 2.49},
#            {'text': 'مع انه ثلاجتي لسى جديدة بس بدي ثلاجة أجدد ', 'start': 309.801, 'duration': 3.279},
#            {'text': 'انا بدي غسالة جديدة ', 'start': 313.207, 'duration': 1.473},
#            {'text': 'كل طلباتكم على راسي يا جيراني', 'start': 314.807, 'duration': 2.381},
#            {'text': 'زي ما اتفقنا بكرا جيبوا كل شئ وانا جاهز في خدمتكم', 'start': 317.333, 'duration': 4.579},
#            {'text': 'بليز كملوا اكلكم', 'start': 322.203, 'duration': 1.797},
#            {'text': 'اي شو هذا الحكي', 'start': 324.145, 'duration': 1.582},
#            {'text': 'انا معك و اعتبرني ايدك اليمين وكلو بحسابه', 'start': 325.836, 'duration': 4.089},
#            {'text': 'هههه', 'start': 329.925, 'duration': 1.075},
#            {'text': 'صوبة كهرباء موديل سنتها', 'start': 331.436, 'duration': 2.672},
#            {'text': 'طيب يا حبيبي اذا موديل سنتها ليش بدك تبدلها', 'start': 334.435, 'duration': 4.67},
#            {'text': 'بدي اللي اجدد منها ', 'start': 339.432, 'duration': 1.346},
#            {'text': 'انا مش مقتنع باللي عم بصير ', 'start': 341.0, 'duration': 2.0},
#            {'text': 'ابو سند الغسالة صرلها سنة مغلبتني ليش ما نجرب', 'start': 343.527, 'duration': 3.835},
#            {'text': 'شوف الناس كلها واقفة طوابير ', 'start': 347.362, 'duration': 1.891},
#            {'text': 'زي ما بدك', 'start': 349.362, 'duration': 0.983},
#            {'text': 'تفضلي سجلي', 'start': 350.726, 'duration': 0.946},
#            {'text': 'يا جماعة الخير هذا البكم فلل استنوا البكم اللي بعده', 'start': 351.999, 'duration': 4.779},
#            {'text': 'اطلع', 'start': 356.923, 'duration': 0.674},
#            {'text': 'يلا روح', 'start': 357.76, 'duration': 1.154},
#            {'text': 'ماما وين بنطلوني الجينز', 'start': 361.53, 'duration': 2.345},
#            {'text': 'لسى ما غسلته ماما', 'start': 364.075, 'duration': 1.292},
#            {'text': 'مش ملحقة عليكم', 'start': 365.367, 'duration': 1.255},
#            {'text': ' صرلي اسبوع بغسل على ايدي', 'start': 366.731, 'duration': 1.782},
#            {'text': 'انهروا', 'start': 368.604, 'duration': 0.638},
#            {'text': 'بابا يزن ورنا بدهم يجي عنا يحضروا المسلسل ', 'start': 369.514, 'duration': 3.486},
#            {'text': 'اي هلكونا صرلهم اسبوع بحضروا عنا', 'start': 373.127, 'duration': 3.58},
#            {'text': 'شو ام سند وينه صاحبكم خلدون والاجهزة الالمانية الحديثة', 'start': 377.016, 'duration': 4.616},
#            {'text': 'هي ام انصاف', 'start': 383.903, 'duration': 1.491},
#            {'text': 'اكيد بدها تقولي انه الاجهزة جاي', 'start': 385.576, 'duration': 2.0},
#            {'text': 'الو', 'start': 387.758, 'duration': 0.529},
#            {'text': 'اه ام انصاف', 'start': 388.614, 'duration': 1.386},
#            {'text': 'شو بتحكي ؟  ', 'start': 394.04, 'duration': 1.255},
#            {'text': 'ما بصدق', 'start': 395.767, 'duration': 1.055},
#            {'text': 'دينا شو في ', 'start': 397.04, 'duration': 1.528},
#            {'text': 'صاحبك', 'start': 398.68, 'duration': 0.874},
#            {'text': 'اخد كل اجهزة الحارة واختفى', 'start': 399.917, 'duration': 2.182},
#            {'text': 'شو بتحكي', 'start': 402.2, 'duration': 0.747},
#            {'text': 'أنا كنت عارف انه الزلمة مش مزبوط', 'start': 403.674, 'duration': 2.272},
#            {'text': 'هلا بروحله على البيت', 'start': 406.218, 'duration': 1.262},
#            {'text': 'راحوا قبلك الجيران', 'start': 407.643, 'duration': 1.473},
#            {'text': 'بس طلع راحل', 'start': 409.207, 'duration': 1.237},
#            {'text': 'وقال ايش', 'start': 410.444, 'duration': 0.91},
#            {'text': 'لسى عليه اجار شهرين مش دافعهم', 'start': 411.554, 'duration': 2.926},
#            {'text': 'شووووو', 'start': 414.571, 'duration': 0.619},
#            {'text': 'تعلمت الدرس', 'start': 416.897, 'duration': 1.019},
#            {'text': ' ما رح اثق بشخص على اساس لبسه وسيارته وشكله وحكيه عن نفسه', 'start': 418.788, 'duration': 4.743},
#            {'text': 'مش كل حدا ببين انه مهتم فينا وفي احتياجاتنا بنثق فيه ثقة عمياء', 'start': 423.622, 'duration': 4.743},
#            {'text': 'من دون ما نكون حاميين حالنا ', 'start': 428.365, 'duration': 1.855},
#            {'text': 'أهم اشي انه الواحد يتعلم من أخطاؤه', 'start': 430.347, 'duration': 2.182},
#            {'text': 'واكيد في ناس حوالينا أهل للثقة', 'start': 432.892, 'duration': 2.926},
#            {'text': 'لو سمحت اديش هذه الثلاجة ؟', 'start': 436.04, 'duration': 1.673},
#            {'text': '١٢٠٠ دينار', 'start': 437.876, 'duration': 0.965},
#            {'text': 'شوووو', 'start': 439.44, 'duration': 0.837},
#            {'text': 'بدي ثلاجتي القديمة', 'start': 441.439, 'duration': 2.672},
#            ]
#
#    srt_content = convert_to_srt(entries)
#    print(srt_content)
#
##    with open('output.srt', 'w', encoding='utf-8') as srt_file:
##        srt_file.write(srt_content)
#
#    print("SRT file created successfully.")
#