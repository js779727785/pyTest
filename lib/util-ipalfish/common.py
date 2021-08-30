import datetime
import io
import json
import os
import random
import hashlib
import time
import uuid
from django.http import JsonResponse, HttpResponse
import pymysql as pymysql
import requests
import urllib3
from DataFactoryBackend.settings import test_base_url, KIDS, ocr_service_url


def get_pw_md5(pw):
    pw = str(pw)
    m = hashlib.md5()
    b = pw.encode(encoding='utf-8')
    m.update(b)
    pw_md5 = m.hexdigest()

    return pw_md5[:16]


def get_timestamp(dt):
    dt = str(dt)
    time_arr = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(time_arr)
    return int(timestamp)


def request_post(data_req):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    if 'cookies' not in data_req:
        data_req['cookies'] = None
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    resp = requests.post(url=data_req['url'], json=data_req['json'], cookies=data_req['cookies'], verify=False)
    # print("请求结果" + str(resp.content))
    data_resp = json.loads(resp.content)
    return data_resp


def user_login(cate, phone, pw):
    data_login = dict()
    data_login['phone'] = phone
    data_login['pw'] = get_pw_md5(pw)
    data_login['cate'] = cate
    data_login['area'] = "86"
    req_login = dict()
    req_login['url'] = test_base_url + '/account/login'
    req_login['json'] = data_login
    resp_login = request_post(req_login)
    return resp_login


def get_vcode_image(path):
    """
    获取图片验证码
    :param phone:
    :return:
    """
    payload = {
        'url': ocr_service_url,
        'json': {
            'image': path
        }
    }
    res_dict = request_post(payload)
    return res_dict.get('result', None)


def readyaml(file_path):
    """
    读取yaml文件
    :param file_path:
    :return:
    """
    if os.path.isfile(file_path):
        fr = open(file_path, 'r')
        import yaml
        yaml_info = yaml.load(fr)
        fr.close()
        return yaml_info
    return None


def writeyaml(file_path, data):
    """
    向yaml文件中写入cookie
    :param file_path:
    :param data:
    :return:
    """
    fr = open(file_path, 'w')
    import yaml
    yaml.dump(data, fr)
    fr.close()


def get_random_phone():
    """
    生成8位随机手机号码
    :return:
    """
    phone = '721'

    def get_8_nums():
        num_str = ''.join(str(random.choice(range(10))) for _ in range(8))
        return num_str

    phone = phone + get_8_nums()
    return phone


def check_stamp(stamps, stamp):
    """
    检查学生是否上过课
    :param stamps:
    :param stamp:
    :return:
    """
    if stamp in stamps:
        d = datetime.datetime.fromtimestamp(stamp)
        datatime = d.strftime("%Y-%m-%d %H:%M:%S")
        raise NoSuccessExceptin('该学生在 ' + datatime + " 已上过课，请换其他时间跳课")


def get_course_time():
    """
    获取上课时间
    获取试听课预约时间点，当前分钟小于30分钟预约半点，如果大于30则预约下一个整点
    :return:
    """
    now = datetime.datetime.now()
    minute = now.minute
    h = time.localtime().tm_hour
    if minute < 30:
        course_time = datetime.datetime.now().replace(hour=h, minute=30, second=0, microsecond=0)
    else:
        course_time = datetime.datetime.now().replace(hour=h + 1, minute=00, second=0, microsecond=0)
    return course_time


def get_name():
    """
    生成用户名
    :return:
    """
    eng_names = ['Aaliyah', 'Aaron', 'Aarushi', 'Abagail', 'Abbey', 'Abbi', 'Abbie', 'Abby', 'Abdul', 'Abdullah', 'Abe',
                 'Abel', 'Abi', 'Abia', 'Abigail', 'Abraham', 'Abram', 'Abrianna', 'Abriel', 'Abrielle', 'Aby',
                 'Acacia', 'Ace', 'Ada', 'Adalia', 'Adalyn', 'Adam', 'Adan', 'Addie', 'Addison', 'Addison', 'Ade',
                 'Adelaide', 'Adele', 'Adelene', 'Adelia', 'Adelina', 'Adeline', 'Aden', 'Adnan', 'Adonis', 'Adreanna',
                 'Adrian', 'Adriana', 'Adrianna', 'Adrianne', 'Adriel', 'Adrienne', 'Aerona', 'Agatha', 'Aggie',
                 'Agnes', 'Ahmad', 'Ahmed', 'Aida', 'Aidan', 'Aiden', 'Aileen', 'Ailsa', 'Aimee', 'Aine', 'Ainsleigh',
                 'Ainsley', 'Ainsley', 'Aisha', 'Aisling', 'Aislinn', 'Ajay', 'Al', 'Alain', 'Alaina', 'Alan', 'Alana',
                 'Alanis', 'Alanna', 'Alannah', 'Alaska', 'Alastair', 'Alayah', 'Alayna', 'Alba', 'Albert', 'Alberta',
                 'Alberto', 'Albie', 'Alden', 'Aldo', 'Aleah', 'Alec', 'Alecia', 'Aleisha', 'Alejandra', 'Alejandro',
                 'Alen', 'Alena', 'Alesandro', 'Alessandra', 'Alessia', 'Alex', 'Alex', 'Alexa', 'Alexander',
                 'Alexandra', 'Alexandria', 'Alexia', 'Alexis', 'Alexis', 'Alexus', 'Alfie', 'Alfonso', 'Alfred',
                 'Alfredo', 'Ali', 'Ali', 'Alia', 'Alice', 'Alicia', 'Alina', 'Alisa', 'Alisha', 'Alison', 'Alissa',
                 'Alistair', 'Alivia', 'Aliyah', 'Aliza', 'Alize', 'Alka', 'Allan', 'Allen', 'Allie', 'Allison', 'Ally',
                 'Allyson', 'Alma', 'Alondra', 'Alonzo', 'Aloysius', 'Alphonso', 'Alton', 'Alvin', 'Alycia',
                 'Alyshialynn', 'Alyson', 'Alyssa', 'Alyssia', 'Amalia', 'Amanda', 'Amani', 'Amara', 'Amari', 'Amari',
                 'Amaris', 'Amaya', 'Amber', 'Amberly', 'Amelia', 'Amelie', 'America', 'Amethyst', 'Amie', 'Amina',
                 'Amir', 'Amirah', 'Amit', 'Amity', 'Amos', 'Amy', 'Amya', 'Ana', 'Anabel', 'Anabelle', 'Anahi',
                 'Anais', 'Anamaria', 'Anand', 'Ananya', 'Anastasia', 'Anderson', 'Andie', 'Andre', 'Andrea', 'Andreas',
                 'Andres', 'Andrew', 'Andromeda', 'Andy', 'Angel', 'Angel', 'Angela', 'Angelia', 'Angelica', 'Angelina',
                 'Angeline', 'Angelique', 'Angelo', 'Angie', 'Angus', 'Anika', 'Anisa', 'Anita', 'Aniya', 'Aniyah',
                 'Anjali', 'Ann', 'Anna', 'Annabel', 'Annabella', 'Annabelle', 'Annabeth', 'Annalisa', 'Annalise',
                 'Anne', 'Anneke', 'Annemarie', 'Annette', 'Annie', 'Annika', 'Annmarie', 'Ansel', 'Anson', 'Anthea',
                 'Anthony', 'Antoinette', 'Anton', 'Antonia', 'Antonio', 'Antony', 'Anuja', 'Anusha', 'Anushka', 'Anya',
                 'Aoibhe', 'Aoibheann', 'Aoife', 'Aphrodite', 'Apollo', 'Apple', 'April', 'Aqua', 'Arabella',
                 'Arabelle', 'Aran', 'Archer', 'Archie', 'Ari', 'Aria', 'Ariadne', 'Ariana', 'Arianna', 'Arianne',
                 'Ariel', 'Ariella', 'Arielle', 'Arisha', 'Arjun', 'Arleen', 'Arlene', 'Arlette', 'Arlo', 'Arman',
                 'Armando', 'Arnold', 'Aron', 'Arran', 'Arrie', 'Art', 'Artemis', 'Arthur', 'Arturo', 'Arun', 'Arwen',
                 'Arwin', 'Arya', 'Asa', 'Asad', 'Ash', 'Asha', 'Ashanti', 'Ashby', 'Asher', 'Ashlee', 'Ashleigh',
                 'Ashley', 'Ashley', 'Ashlie', 'Ashlyn', 'Ashlynn', 'Ashton', 'Ashton', 'Ashvini', 'Asia', 'Asma',
                 'Aspen', 'Aspen', 'Aston', 'Astrid', 'Athan', 'Athena', 'Athene', 'Atticus', 'Aubreanna', 'Aubree',
                 'Aubrey', 'Aubrey', 'Audra', 'Audrey', 'Audrina', 'Audwin', 'August', 'Augustina', 'Augustus',
                 'Aurelia', 'Aurora', 'Austen', 'Austin', 'Autumn', 'Ava', 'Avalon', 'Avery', 'Avery', 'Avril', 'Axel',
                 'Aya', 'Ayaan', 'Ayana', 'Ayanna', 'Ayden', 'Ayesha', 'Ayisha', 'Ayla', 'Azalea', 'Azaria', 'Azariah',
                 'Bailey', 'Bailey', 'Barack', 'Barbara', 'Barbie', 'Barclay', 'Barnaby', 'Barney', 'Barrett', 'Barron',
                 'Barry', 'Bart', 'Bartholomew', 'Basil', 'Bastian', 'Baxter', 'Bay', 'Bay', 'Baylee', 'Baylor', 'Bea',
                 'Bear', 'Beatrice', 'Beatrix', 'Beau', 'Becca', 'Beccy', 'Beck', 'Beckett', 'Becky', 'Belinda',
                 'Bella', 'Bellamy', 'Bellatrix', 'Belle', 'Ben', 'Benedict', 'Benita', 'Benjamin', 'Benji', 'Benjy',
                 'Bennett', 'Bennie', 'Benny', 'Benson', 'Bentley', 'Bently', 'Bernadette', 'Bernard', 'Bernardo',
                 'Bernice', 'Bernie', 'Bert', 'Bertha', 'Bertie', 'Bertram', 'Beryl', 'Bess', 'Beth', 'Bethan',
                 'Bethanie', 'Bethany', 'Betsy', 'Bettina', 'Betty', 'Bev', 'Bevan', 'Beverly', 'Beyonce', 'Bianca',
                 'Bill', 'Billie', 'Billy', 'Bjorn', 'Bladen', 'Blain', 'Blaine', 'Blair', 'Blair', 'Blaire', 'Blaise',
                 'Blake', 'Blake', 'Blakely', 'Blanche', 'Blaze', 'Blaze', 'Blessing', 'Bliss', 'Bloom', 'Blossom',
                 'Blue', 'Blythe', 'Bob', 'Bobbi', 'Bobbie', 'Bobby', 'Bobby', 'Bodie', 'Bonita', 'Bonnie', 'Bonquesha',
                 'Boris', 'Boston', 'Bowen', 'Boyd', 'Brad', 'Braden', 'Bradford', 'Bradley', 'Bradwin', 'Brady',
                 'Braeden', 'Braelyn', 'Bram', 'Branden', 'Brandi', 'Brandon', 'Brandy', 'Brantley', 'Braxton',
                 'Brayan', 'Brayden', 'Braydon', 'Braylee', 'Braylon', 'Brea', 'Breanna', 'Bree', 'Breeze', 'Brenda',
                 'Brendan', 'Brenden', 'Brendon', 'Brenna', 'Brennan', 'Brent', 'Brenton', 'Bret', 'Brett', 'Brevin',
                 'Brevyn', 'Bria', 'Brian', 'Briana', 'Brianna', 'Brianne', 'Briar', 'Brice', 'Bridget', 'Bridgette',
                 'Bridie', 'Bridie', 'Briella', 'Brielle', 'Brighton', 'Brigid', 'Briley', 'Brinley', 'Brinley',
                 'Briony', 'Brisa', 'Bristol', 'Britney', 'Britt', 'Brittany', 'Brittney', 'Brock', 'Brodie', 'Brody',
                 'Brogan', 'Brogan', 'Bronagh', 'Bronson', 'Bronte', 'Bronwen', 'Bronwyn', 'Brook', 'Brooke',
                 'Brooklyn', 'Brooklynn', 'Brooks', 'Bruce', 'Bruno', 'Bryan', 'Bryanna', 'Bryant', 'Bryce', 'Bryden',
                 'Brydon', 'Brylee', 'Bryn', 'Brynlee', 'Brynn', 'Bryon', 'Bryony', 'Bryson', 'Buck', 'Buddy', 'Bunty',
                 'Burt', 'Burton', 'Buster', 'Butch', 'Byron', 'Cadby', 'Cade', 'Caden', 'Cadence', 'Cael', 'Caelan',
                 'Caesar', 'Cai', 'Caiden', 'Cailin', 'Cain', 'Caitlan', 'Caitlin', 'Caitlyn', 'Caius', 'Cal', 'Cale',
                 'Caleb', 'Caleigh', 'Calhoun', 'Cali', 'Calista', 'Callan', 'Callen', 'Callie', 'Calliope', 'Callista',
                 'Callum', 'Calum', 'Calvin', 'Calypso', 'Cam', 'Cambria', 'Camden', 'Cameron', 'Cameron', 'Cami',
                 'Camila', 'Camilla', 'Camille', 'Campbell', 'Camron', 'Camryn', 'Candace', 'Candice', 'Candis',
                 'Candy', 'Caoimhe', 'Caprice', 'Cara', 'Carey', 'Carina', 'Caris', 'Carissa', 'Carl', 'Carla',
                 'Carlene', 'Carley', 'Carlie', 'Carlisle', 'Carlos', 'Carlton', 'Carly', 'Carlynn', 'Carmel',
                 'Carmela', 'Carmen', 'Carol', 'Carole', 'Carolina', 'Caroline', 'Carolyn', 'Carrie', 'Carsen',
                 'Carson', 'Carter', 'Carter', 'Cary', 'Carys', 'Casey', 'Casey', 'Cash', 'Cason', 'Casper',
                 'Cassandra', 'Cassia', 'Cassidy', 'Cassie', 'Cassius', 'Castiel', 'Castor', 'Cat', 'Catalina', 'Cate',
                 'Caterina', 'Cathal', 'Cathalina', 'Catherine', 'Cathleen', 'Cathy', 'Catlin', 'Cato', 'Catrina',
                 'Catriona', 'Cavan', 'Cayden', 'Caydon', 'Cayla', 'Cece', 'Cecelia', 'Cecil', 'Cecilia', 'Cecily',
                 'Cedric', 'Celeste', 'Celestia', 'Celestine', 'Celia', 'Celina', 'Celine', 'Celise', 'Cerise', 'Cerys',
                 'Cesar', 'Chad', 'Chance', 'Chandler', 'Chanel', 'Chanelle', 'Channing', 'Chantal', 'Chantelle',
                 'Charis', 'Charissa', 'Charity', 'Charlene', 'Charles', 'Charley', 'Charley', 'Charlie', 'Charlie',
                 'Charlize', 'Charlotte', 'Charlton', 'Charmaine', 'Chase', 'Chastity', 'Chaz', 'Che', 'Chelsea',
                 'Chelsey', 'Chenai', 'Chenille', 'Cher', 'Cheri', 'Cherie', 'Cherry', 'Cheryl', 'Chesney', 'Chester',
                 'Chevy', 'Cheyanne', 'Cheyenne', 'Chiara', 'Chip', 'Chloe', 'Chris', 'Chris', 'Chrissy', 'Christa',
                 'Christabel', 'Christal', 'Christen', 'Christi', 'Christian', 'Christiana', 'Christie', 'Christina',
                 'Christine', 'Christopher', 'Christy', 'Chrystal', 'Chuck', 'Cian', 'Ciara', 'Ciaran', 'Cici', 'Ciel',
                 'Cierra', 'Cillian', 'Cindy', 'Claire', 'Clancy', 'Clara', 'Clarabelle', 'Clare', 'Clarence',
                 'Clarice', 'Claris', 'Clarissa', 'Clarisse', 'Clarity', 'Clark', 'Clary', 'Claude', 'Claudette',
                 'Claudia', 'Claudine', 'Clay', 'Clayton', 'Clea', 'Clement', 'Clementine', 'Cleo', 'Cleopatra',
                 'Cliff', 'Clifford', 'Clifton', 'Clint', 'Clinton', 'Clive', 'Clodagh', 'Clotilde', 'Clover', 'Clyde',
                 'Coby', 'Coco', 'Cody', 'Cohen', 'Colby', 'Cole', 'Colette', 'Colin', 'Colleen', 'Collin', 'Colm',
                 'Colt', 'Colton', 'Conan', 'Conner', 'Connie', 'Connor', 'Conor', 'Conrad', 'Constance', 'Constantine',
                 'Cooper', 'Cora', 'Coral', 'Coralie', 'Coraline', 'Corbin', 'Cordelia', 'Corey', 'Cori', 'Corina',
                 'Corinne', 'Cormac', 'Cornelia', 'Cornelius', 'Corra', 'Cory', 'Cosette', 'Courtney', 'Craig',
                 'Cressida', 'Cristal', 'Cristian', 'Cristina', 'Cristobal', 'Crosby', 'Cruz', 'Crystal', 'Cullen',
                 'Curt', 'Curtis', 'Cuthbert', 'Cyndi', 'Cynthia', 'Cyril', 'Cyrus', 'Dacey', 'Dagmar', 'Dahlia',
                 'Daire', 'Daisy', 'Dakota', 'Dakota', 'Dale', 'Dallas', 'Dalton', 'Damian', 'Damien', 'Damion',
                 'Damon', 'Dan', 'Dana', 'Dana', 'Dane', 'Danette', 'Dani', 'Danica', 'Daniel', 'Daniela', 'Daniella',
                 'Danielle', 'Danika', 'Danny', 'Dante', 'Daphne', 'Dara', 'Dara', 'Daragh', 'Darby', 'Darcey',
                 'Darcie', 'Darcy', 'Darcy', 'Daren', 'Daria', 'Darian', 'Darin', 'Dario', 'Darius', 'Darla', 'Darlene',
                 'Darnell', 'Darragh', 'Darrel', 'Darrell', 'Darren', 'Darrin', 'Darryl', 'Darryn', 'Darwin', 'Daryl',
                 'Dash', 'Dashawn', 'Dasia', 'Dave', 'David', 'Davida', 'Davin', 'Davina', 'Davion', 'Davis', 'Dawn',
                 'Dawson', 'Dax', 'Daxter', 'Daxton', 'Dayna', 'Daysha', 'Dayton', 'Deacon', 'Dean', 'Deana', 'Deandra',
                 'Deandre', 'Deann', 'Deanna', 'Deanne', 'Deb', 'Debbie', 'Debby', 'Debora', 'Deborah', 'Debra',
                 'Declan', 'Dee', 'Deedee', 'Deena', 'Deepak', 'Deidre', 'Deirdre', 'Deja', 'Delaney', 'Delanie',
                 'Delany', 'Delbert', 'Delia', 'Delilah', 'Della', 'Delores', 'Delphine', 'Demetria', 'Demetrius',
                 'Demi', 'Dena', 'Denis', 'Denise', 'Dennis', 'Denny', 'Denver', 'Denzel', 'Deon', 'Derek', 'Dermot',
                 'Derrick', 'Deshaun', 'Deshawn', 'Desiree', 'Desmond', 'Destinee', 'Destiny', 'Dev', 'Devin', 'Devlin',
                 'Devon', 'Dewayne', 'Dewey', 'Dexter', 'Diamond', 'Diana', 'Diane', 'Dianna', 'Dianne', 'Diarmuid',
                 'Dick', 'Dido', 'Diego', 'Dilan', 'Dillon', 'Dimitri', 'Dina', 'Dinesh', 'Dino', 'Dion', 'Dionne',
                 'Dior', 'Dirk', 'Dixie', 'Django', 'Dmitri', 'Dolly', 'Dolores', 'Dominic', 'Dominick', 'Dominique',
                 'Don', 'Donald', 'Donna', 'Donnie', 'Donovan', 'Dora', 'Doreen', 'Dorian', 'Doris', 'Dorothy', 'Dot',
                 'Doug', 'Douglas', 'Doyle', 'Drake', 'Drew', 'Drew', 'Duane', 'Duke', 'Dulce', 'Duncan', 'Dustin',
                 'Dwayne', 'Dwight', 'Dylan', 'Eabha', 'Eamon', 'Earl', 'Earnest', 'Eason', 'Easton', 'Ebony', 'Echo',
                 'Ed', 'Eddie', 'Eddy', 'Eden', 'Eden', 'Edgar', 'Edie', 'Edison', 'Edith', 'Edmund', 'Edna', 'Edouard',
                 'Edric', 'Edsel', 'Eduardo', 'Edward', 'Edwardo', 'Edwin', 'Edwina', 'Effie', 'Efrain', 'Efren',
                 'Egan', 'Egon', 'Eileen', 'Eilidh', 'Eimear', 'Elaina', 'Elaine', 'Elana', 'Eleanor', 'Electra',
                 'Elektra', 'Elena', 'Eli', 'Eliana', 'Elias', 'Elijah', 'Elin', 'Elina', 'Elinor', 'Eliot', 'Elisa',
                 'Elisabeth', 'Elise', 'Elisha', 'Eliza', 'Elizabeth', 'Ella', 'Elle', 'Ellen', 'Ellery', 'Ellie',
                 'Ellington', 'Elliot', 'Elliott', 'Ellis', 'Ellis', 'Elly', 'Elmer', 'Elmo', 'Elodie', 'Eloise',
                 'Elora', 'Elsa', 'Elsie', 'Elspeth', 'Elton', 'Elva', 'Elvira', 'Elvis', 'Elwyn', 'Elysia', 'Elyza',
                 'Emanuel', 'Emanuela', 'Ember', 'Emelda', 'Emely', 'Emer', 'Emerald', 'Emerson', 'Emerson', 'Emery',
                 'Emet', 'Emil', 'Emilee', 'Emilia', 'Emiliano', 'Emilie', 'Emilio', 'Emily', 'Emma', 'Emmalee',
                 'Emmaline', 'Emmalyn', 'Emmanuel', 'Emmanuelle', 'Emmeline', 'Emmerson', 'Emmet', 'Emmett', 'Emmie',
                 'Emmy', 'Enid', 'Ennio', 'Enoch', 'Enrique', 'Enya', 'Enzo', 'Eoghan', 'Eoin', 'Eric', 'Erica',
                 'Erick', 'Erik', 'Erika', 'Erin', 'Eris', 'Ernest', 'Ernesto', 'Ernie', 'Errol', 'Ervin', 'Erwin',
                 'Eryn', 'Esmay', 'Esme', 'Esmeralda', 'Esparanza', 'Esperanza', 'Esteban', 'Estee', 'Estelle', 'Ester',
                 'Esther', 'Estrella', 'Ethan', 'Ethel', 'Ethen', 'Etienne', 'Euan', 'Euen', 'Eugene', 'Eugenie',
                 'Eunice', 'Eustace', 'Eva', 'Evan', 'Evangelina', 'Evangeline', 'Evangelos', 'Eve', 'Evelin', 'Evelyn',
                 'Evelyn', 'Everett', 'Everly', 'Evie', 'Evita', 'Ewan', 'Ezekiel', 'Ezio', 'Ezra', 'Fabian', 'Fabio',
                 'Fabrizia', 'Faisal', 'Faith', 'Fallon', 'Fanny', 'Farah', 'Farley', 'Farrah', 'Fatima', 'Fawn', 'Fay',
                 'Faye', 'Febian', 'Felicia', 'Felicity', 'Felipe', 'Felix', 'Fergus', 'Fern', 'Fernand', 'Fernanda',
                 'Fernando', 'Ffion', 'Fidel', 'Fifi', 'Finbar', 'Finlay', 'Finley', 'Finn', 'Finnian', 'Finnigan',
                 'Fiona', 'Fionn', 'Fletcher', 'Fleur', 'Flick', 'Flo', 'Flora', 'Florence', 'Floyd', 'Flynn', 'Ford',
                 'Forest', 'Forrest', 'Foster', 'Fox', 'Fran', 'Frances', 'Francesca', 'Francesco', 'Francine',
                 'Francis', 'Francisco', 'Frank', 'Frankie', 'Frankie', 'Franklin', 'Franklyn', 'Fraser', 'Fred',
                 'Freda', 'Freddie', 'Freddy', 'Frederick', 'Fredrick', 'Freya', 'Frida', 'Fritz', 'Gabby', 'Gabe',
                 'Gabriel', 'Gabriela', 'Gabriella', 'Gabrielle', 'Gael', 'Gaelan', 'Gage', 'Gail', 'Gale', 'Galen',
                 'Gannon', 'Gareth', 'Garman', 'Garnet', 'Garrett', 'Garrison', 'Garry', 'Garth', 'Gary', 'Gaston',
                 'Gavin', 'Gayle', 'Gaynor', 'Geena', 'Gemma', 'Gena', 'Gene', 'Genesis', 'Genevieve', 'Geoff',
                 'Geoffrey', 'George', 'Georgette', 'Georgia', 'Georgie', 'Georgina', 'Geraint', 'Gerald', 'Geraldine',
                 'Gerard', 'Gerardo', 'Germain', 'Gerry', 'Gert', 'Gertrude', 'Gia', 'Gian', 'Gianna', 'Gibson',
                 'Gideon', 'Gigi', 'Gil', 'Gilbert', 'Gilberto', 'Giles', 'Gillian', 'Gina', 'Ginger', 'Ginny', 'Gino',
                 'Giorgio', 'Giovanna', 'Giovanni', 'Gisela', 'Giselle', 'Gisselle', 'Gladys', 'Glen', 'Glenda',
                 'Glenn', 'Glenys', 'Gloria', 'Glyndwr', 'Glynis', 'Godfrey', 'Godric', 'Godwin', 'Golda', 'Goldie',
                 'Gonzalo', 'Gordon', 'Grace', 'Gracelyn', 'Gracie', 'Grady', 'Graeme', 'Graham', 'Grainne', 'Grant',
                 'Grayson', 'Greg', 'Gregg', 'Gregor', 'Gregory', 'Greta', 'Gretchen', 'Grey', 'Greyson', 'Griffin',
                 'Griselda', 'Guadalupe', 'Guillermo', 'Guinevere', 'Gunnar', 'Gunner', 'Gus', 'Gustav', 'Gustavo',
                 'Guy', 'Gwen', 'Gwendolyn', 'Gwyneth', 'Habiba', 'Haden', 'Hadley', 'Haiden', 'Hailee', 'Hailey',
                 'Hal', 'Haleigh', 'Haley', 'Halle', 'Hallie', 'Hamish', 'Han', 'Hank', 'Hanna', 'Hannah', 'Hans',
                 'Harlan', 'Harley', 'Harley', 'Harmony', 'Harold', 'Harper', 'Harriet', 'Harris', 'Harrison', 'Harry',
                 'Harvey', 'Hassan', 'Hattie', 'Haven', 'Hayden', 'Hayden', 'Hayes', 'Haylee', 'Hayley', 'Hazel',
                 'Hazeline', 'Heath', 'Heather', 'Heaven', 'Hector', 'Heidi', 'Helen', 'Helena', 'Helene', 'Helga',
                 'Helina', 'Hendrik', 'Hendrix', 'Henley', 'Henri', 'Henrietta', 'Henry', 'Hepsiba', 'Hera', 'Herbert',
                 'Herman', 'Hermione', 'Hester', 'Heston', 'Hetty', 'Hilary', 'Hilary', 'Hilda', 'Hillary', 'Holden',
                 'Hollie', 'Holly', 'Homer', 'Honesty', 'Honey', 'Honor', 'Honour', 'Hope', 'Horace', 'Horatio',
                 'Howard', 'Hubert', 'Hudson', 'Hugh', 'Hugo', 'Humberto', 'Humphrey', 'Hunter', 'Huw', 'Hyacinth',
                 'Hywel', 'Iain', 'Ian', 'Ianthe', 'Ianto', 'Ibrahim', 'Ida', 'Idris', 'Ieuan', 'Iggy', 'Ignacio',
                 'Igor', 'Ike', 'Ila', 'Ilene', 'Iliana', 'Ilona', 'Ilse', 'Imani', 'Imelda', 'Imogen', 'Imran',
                 'India', 'Indiana', 'Indie', 'Indigo', 'Indira', 'Ines', 'Ingrid', 'Inigo', 'Iona', 'Ira', 'Ira',
                 'Irene', 'Irina', 'Iris', 'Irma', 'Irvin', 'Irving', 'Irwin', 'Isa', 'Isaac', 'Isabel', 'Isabell',
                 'Isabella', 'Isabelle', 'Isadora', 'Isaiah', 'Isha', 'Isiah', 'Isidore', 'Isis', 'Isla', 'Ismael',
                 'Isobel', 'Isolde', 'Israel', 'Issac', 'Itzel', 'Ivan', 'Ivana', 'Ivor', 'Ivy', 'Iyanna', 'Izabella',
                 'Izidora', 'Izzie', 'Izzy', 'Jace', 'Jacinda', 'Jacinta', 'Jack', 'Jackie', 'Jackie', 'Jackson',
                 'Jacob', 'Jacoby', 'Jacqueline', 'Jacquelyn', 'Jacques', 'Jada', 'Jade', 'Jaden', 'Jaden', 'Jadon',
                 'Jadyn', 'Jaelynn', 'Jagger', 'Jago', 'Jai', 'Jaida', 'Jaiden', 'Jaime', 'Jaime', 'Jak', 'Jake',
                 'Jakob', 'Jalen', 'Jamal', 'James', 'Jameson', 'Jamie', 'Jamie', 'Jamison', 'Jamiya', 'Jan', 'Jan',
                 'Jana', 'Jancis', 'Jane', 'Janelle', 'Janessa', 'Janet', 'Janette', 'Jania', 'Janice', 'Janie',
                 'Janine', 'Janis', 'Janiya', 'January', 'Jaqueline', 'Jared', 'Jarod', 'Jarrett', 'Jarrod', 'Jarvis',
                 'Jase', 'Jasmin', 'Jasmine', 'Jason', 'Jasper', 'Javier', 'Javon', 'Jax', 'Jaxon', 'Jaxson', 'Jay',
                 'Jaya', 'Jayce', 'Jayda', 'Jayden', 'Jayden', 'Jaydon', 'Jayla', 'Jaylen', 'Jaylene', 'Jaylin',
                 'Jaylinn', 'Jaylon', 'Jaylynn', 'Jayne', 'Jayson', 'Jazlyn', 'Jazmin', 'Jazmine', 'Jazz', 'Jean',
                 'Jeanette', 'Jeanine', 'Jeanne', 'Jeannette', 'Jeannie', 'Jeannine', 'Jeb', 'Jebediah', 'Jed',
                 'Jediah', 'Jedidiah', 'Jeff', 'Jefferson', 'Jeffery', 'Jeffrey', 'Jeffry', 'Jemima', 'Jemma', 'Jen',
                 'Jena', 'Jenelle', 'Jenessa', 'Jenna', 'Jennette', 'Jenni', 'Jennie', 'Jennifer', 'Jenny', 'Jensen',
                 'Jensen', 'Jenson', 'Jerald', 'Jeremiah', 'Jeremy', 'Jeri', 'Jericho', 'Jermaine', 'Jerome', 'Jerri',
                 'Jerry', 'Jess', 'Jessa', 'Jesse', 'Jessica', 'Jessie', 'Jessie', 'Jesus', 'Jet', 'Jet', 'Jethro',
                 'Jett', 'Jewel', 'Jill', 'Jillian', 'Jim', 'Jimmie', 'Jimmy', 'Jo', 'Joachim', 'Joan', 'Joann',
                 'Joanna', 'Joanne', 'Joaquin', 'Jocelyn', 'Jodi', 'Jodie', 'Jody', 'Jody', 'Joe', 'Joel', 'Joelle',
                 'Joey', 'Johan', 'Johanna', 'John', 'Johnathan', 'Johnathon', 'Johnnie', 'Johnny', 'Joleen', 'Jolene',
                 'Jolie', 'Jon', 'Jonah', 'Jonas', 'Jonathan', 'Jonathon', 'Joni', 'Jonty', 'Jordan', 'Jordan',
                 'Jordana', 'Jordon', 'Jordy', 'Jordyn', 'Jorge', 'Jorja', 'Jose', 'Joselyn', 'Joseph', 'Josephine',
                 'Josh', 'Joshua', 'Josiah', 'Josie', 'Josue', 'Jovan', 'Joy', 'Joyce', 'Juan', 'Juanita', 'Judah',
                 'Judas', 'Judd', 'Jude', 'Jude', 'Judith', 'Judy', 'Jules', 'Julia', 'Julian', 'Juliana', 'Julianna',
                 'Julianne', 'Julie', 'Julienne', 'Juliet', 'Juliette', 'Julio', 'Julissa', 'Julius', 'July', 'June',
                 'Juniper', 'Juno', 'Justice', 'Justice', 'Justin', 'Justina', 'Justine', 'Kacey', 'Kade', 'Kaden',
                 'Kadence', 'Kai', 'Kaiden', 'Kaidence', 'Kailey', 'Kailyn', 'Kaine', 'Kaitlin', 'Kaitlyn', 'Kaitlynn',
                 'Kale', 'Kalea', 'Kaleb', 'Kaleigh', 'Kali', 'Kalia', 'Kalista', 'Kallie', 'Kamala', 'Kameron',
                 'Kamryn', 'Kane', 'Kara', 'Karen', 'Kari', 'Karin', 'Karina', 'Karissa', 'Karl', 'Karla', 'Karlee',
                 'Karly', 'Karolina', 'Karson', 'Karyn', 'Kasey', 'Kash', 'Kasper', 'Kassandra', 'Kassidy', 'Kassie',
                 'Kat', 'Katara', 'Katarina', 'Kate', 'Katelyn', 'Katelynn', 'Katerina', 'Katharine', 'Katherine',
                 'Kathleen', 'Kathryn', 'Kathy', 'Katia', 'Katie', 'Katlyn', 'Katniss', 'Katrina', 'Katy', 'Katya',
                 'Kay', 'Kaya', 'Kayden', 'Kaye', 'Kayla', 'Kaylee', 'Kayleigh', 'Kaylen', 'Kayley', 'Kaylie', 'Kaylin',
                 'Kayson', 'Keanu', 'Keara', 'Keaton', 'Kedrick', 'Keegan', 'Keeley', 'Keely', 'Keenan', 'Keira',
                 'Keisha', 'Keith', 'Kelis', 'Kellan', 'Kellen', 'Kelley', 'Kelli', 'Kellie', 'Kellin', 'Kelly',
                 'Kelly', 'Kelsey', 'Kelsie', 'Kelvin', 'Ken', 'Kendall', 'Kendall', 'Kendra', 'Kendrick', 'Kenna',
                 'Kennedy', 'Kennedy', 'Kenneth', 'Kenny', 'Kent', 'Kenton', 'Kenzie', 'Kera', 'Keri', 'Kerian',
                 'Kerri', 'Kerry', 'Kerry', 'Kevin', 'Khalid', 'Khalil', 'Kia', 'Kian', 'Kiana', 'Kiara', 'Kiefer',
                 'Kiera', 'Kieran', 'Kieron', 'Kierra', 'Kiersten', 'Kiki', 'Kiley', 'Killian', 'Kim', 'Kim',
                 'Kimberlee', 'Kimberley', 'Kimberly', 'Kimbriella', 'Kimmy', 'Kingsley', 'Kingston', 'Kinley',
                 'Kinsey', 'Kinsley', 'Kip', 'Kira', 'Kiran', 'Kirby', 'Kirk', 'Kirsten', 'Kirstin', 'Kirsty', 'Kit',
                 'Kitty', 'Kizzy', 'Klaus', 'Klay', 'Kloe', 'Knox', 'Kobe', 'Koby', 'Kody', 'Kolby', 'Kora', 'Kori',
                 'Kourtney', 'Kris', 'Kris', 'Krish', 'Krista', 'Kristen', 'Kristi', 'Kristian', 'Kristie', 'Kristin',
                 'Kristina', 'Kristine', 'Kristoff', 'Kristopher', 'Kristy', 'Krystal', 'Kurt', 'Kurtis', 'Kye', 'Kyla',
                 'Kylar', 'Kyle', 'Kylee', 'Kyleigh', 'Kylen', 'Kyler', 'Kylie', 'Kyra', 'Kyran', 'Kyrin', 'Kyron',
                 'Lacey', 'Lacey', 'Lachlan', 'Lacie', 'Lacy', 'Ladonna', 'Laila', 'Lainey', 'Lake', 'Lakyn', 'Lala',
                 'Lamar', 'Lamont', 'Lana', 'Lance', 'Landen', 'Landon', 'Landyn', 'Lane', 'Laney', 'Langdon',
                 'Langston', 'Lara', 'Larissa', 'Larry', 'Lars', 'Latoya', 'Laura', 'Laurel', 'Lauren', 'Laurence',
                 'Laurie', 'Laurie', 'Lauryn', 'Lavana', 'Lavender', 'Lavinia', 'Lawrence', 'Lawson', 'Layla', 'Layne',
                 'Layton', 'Lea', 'Leaf', 'Leah', 'Leandra', 'Leandro', 'Leann', 'Leanna', 'Leanne', 'Lebron', 'Lee',
                 'Lee', 'Leela', 'Leena', 'Leia', 'Leigh', 'Leigh', 'Leighton', 'Leila', 'Leilani', 'Lela', 'Leland',
                 'Lena', 'Lennie', 'Lennon', 'Lennox', 'Lenny', 'Lenore', 'Leo', 'Leon', 'Leona', 'Leonard', 'Leonardo',
                 'Leonel', 'Leonie', 'Leopold', 'Leora', 'Leroy', 'Les', 'Lesley', 'Leslie', 'Leslie', 'Lesly',
                 'Lester', 'Leticia', 'Letitia', 'Lettie', 'Leuan', 'Lev', 'Leven', 'Levi', 'Lewis', 'Lex', 'Lexi',
                 'Lexia', 'Lexie', 'Lexis', 'Leyla', 'Lia', 'Liam', 'Liana', 'Lianne', 'Libbie', 'Libby', 'Liberty',
                 'Lidia', 'Lief', 'Liesl', 'Lila', 'Lilac', 'Lilah', 'Lili', 'Lilian', 'Liliana', 'Lilita', 'Lilith',
                 'Lillia', 'Lillian', 'Lillie', 'Lilly', 'Lily', 'Lina', 'Lincoln', 'Linda', 'Lindsay', 'Lindsey',
                 'Lindy', 'Link', 'Linus', 'Lionel', 'Lisa', 'Lisandro', 'Lisette', 'Liv', 'Livia', 'Livvy', 'Liz',
                 'Liza', 'Lizbeth', 'Lizette', 'Lizzie', 'Lizzy', 'Lloyd', 'Lochlan', 'Logan', 'Logan', 'Lois', 'Loki',
                 'Lola', 'Lolita', 'London', 'London', 'Lonnie', 'Lora', 'Loran', 'Lorcan', 'Lorelei', 'Loren', 'Loren',
                 'Lorena', 'Lorenzo', 'Loretta', 'Lori', 'Lorie', 'Loris', 'Lorna', 'Lorraine', 'Lorri', 'Lorrie',
                 'Lottie', 'Lotus', 'Lou', 'Lou', 'Louella', 'Louie', 'Louis', 'Louisa', 'Louise', 'Lowell', 'Luann',
                 'Luca', 'Lucas', 'Lucia', 'Lucian', 'Luciana', 'Luciano', 'Lucie', 'Lucille', 'Lucinda', 'Lucky',
                 'Lucy', 'Luigi', 'Luis', 'Luisa', 'Lukas', 'Luke', 'Lulu', 'Luna', 'Lupita', 'Luther', 'Luz', 'Lydia',
                 'Lyla', 'Lyle', 'Lynda', 'Lyndon', 'Lyndsey', 'Lynette', 'Lynn', 'Lynn', 'Lynne', 'Lynnette', 'Lynsey',
                 'Lyra', 'Lyric', 'Lysander', 'Mabel', 'Macey', 'Macie', 'Mack', 'Mackenzie', 'Macy', 'Madalyn',
                 'Maddie', 'Maddison', 'Maddox', 'Maddy', 'Madeleine', 'Madeline', 'Madelyn', 'Madison', 'Madisyn',
                 'Madonna', 'Madyson', 'Mae', 'Maeve', 'Magda', 'Magdalena', 'Magdalene', 'Maggie', 'Magnus', 'Maia',
                 'Maire', 'Mairead', 'Maisie', 'Maison', 'Maisy', 'Maja', 'Makayla', 'Makenna', 'Makenzie', 'Malachi',
                 'Malakai', 'Malcolm', 'Malia', 'Malik', 'Malina', 'Malinda', 'Mallory', 'Malloy', 'Malory', 'Mandy',
                 'Manny', 'Manuel', 'Manuela', 'Mara', 'Marc', 'Marcel', 'Marcela', 'Marcella', 'Marcelle', 'Marci',
                 'Marcia', 'Marcie', 'Marco', 'Marcos', 'Marcus', 'Marcy', 'Margaret', 'Margarita', 'Margaux', 'Marge',
                 'Margie', 'Margo', 'Margot', 'Margret', 'Maria', 'Mariah', 'Mariam', 'Marian', 'Mariana', 'Marianna',
                 'Marianne', 'Maribel', 'Marie', 'Mariela', 'Mariella', 'Marik', 'Marilyn', 'Marina', 'Mario', 'Marion',
                 'Marion', 'Marisa', 'Marisol', 'Marissa', 'Maritza', 'Marjorie', 'Mark', 'Marla', 'Marlee', 'Marlena',
                 'Marlene', 'Marley', 'Marley', 'Marlon', 'Marnie', 'Marquis', 'Marsha', 'Marshall', 'Martha', 'Martin',
                 'Martina', 'Marty', 'Martyn', 'Marvin', 'Mary', 'Maryam', 'Maryann', 'Marybeth', 'Masie', 'Mason',
                 'Massimo', 'Mat', 'Mateo', 'Mathew', 'Matilda', 'Matt', 'Matthew', 'Matthias', 'Maude', 'Maura',
                 'Maureen', 'Maurice', 'Mauricio', 'Maverick', 'Mavis', 'Max', 'Maxim', 'Maximilian', 'Maximus',
                 'Maxine', 'Maxwell', 'May', 'Maya', 'Mazie', 'Mckayla', 'Mckenna', 'Mckenzie', 'Mea', 'Meadow',
                 'Meagan', 'Meera', 'Meg', 'Megan', 'Meghan', 'Mehdi', 'Mehtab', 'Mei', 'Mekhi', 'Mel', 'Mel',
                 'Melanie', 'Melina', 'Melinda', 'Melissa', 'Melody', 'Melvin', 'Mercedes', 'Mercy', 'Meredith',
                 'Merick', 'Merida', 'Mervyn', 'Meryl', 'Mia', 'Micah', 'Michael', 'Michaela', 'Micheal', 'Michele',
                 'Michelle', 'Mick', 'Mickey', 'Miguel', 'Mika', 'Mikaela', 'Mikayla', 'Mike', 'Mikey', 'Mikhaela',
                 'Mila', 'Milan', 'Mildred', 'Milena', 'Miles', 'Miley', 'Miller', 'Millicent', 'Millie', 'Milly',
                 'Milo', 'Milton', 'Mimi', 'Mina', 'Mindy', 'Minerva', 'Minnie', 'Mira', 'Mirabel', 'Mirabelle',
                 'Miracle', 'Miranda', 'Miriam', 'Mirielle', 'Misha', 'Missie', 'Misty', 'Mitch', 'Mitchell', 'Mitt',
                 'Mitzi', 'Moe', 'Mohamed', 'Mohammad', 'Mohammed', 'Moira', 'Moises', 'Mollie', 'Molly', 'Mona',
                 'Monica', 'Monika', 'Monique', 'Montana', 'Monte', 'Montserrat', 'Monty', 'Mordecai', 'Morgan',
                 'Morgan', 'Morgana', 'Morris', 'Moses', 'Moya', 'Muhammad', 'Muriel', 'Murphy', 'Murray', 'Mya',
                 'Myfanwy', 'Myla', 'Myles', 'Myra', 'Myrna', 'Myron', 'Myrtle', 'Nadene', 'Nadia', 'Nadine', 'Naja',
                 'Nala', 'Nana', 'Nancy', 'Nanette', 'Naomi', 'Nash', 'Nasir', 'Natalia', 'Natalie', 'Natasha', 'Nate',
                 'Nath', 'Nathan', 'Nathanael', 'Nathaniel', 'Naya', 'Nayeli', 'Neal', 'Ned', 'Nehemiah', 'Neil',
                 'Nell', 'Nellie', 'Nelly', 'Nelson', 'Nena', 'Nerissa', 'Nesbit', 'Nessa', 'Nestor', 'Nevaeh', 'Neve',
                 'Neville', 'Nevin', 'Nia', 'Niall', 'Niamh', 'Nichola', 'Nicholas', 'Nichole', 'Nick', 'Nicki',
                 'Nickolas', 'Nicky', 'Nicky', 'Nico', 'Nicola', 'Nicolas', 'Nicole', 'Nicolette', 'Nieve', 'Nigel',
                 'Niki', 'Nikita', 'Nikki', 'Niklaus', 'Nikolai', 'Nikolas', 'Nila', 'Nile', 'Nils', 'Nina', 'Nishka',
                 'Noah', 'Noe', 'Noel', 'Noelle', 'Noemi', 'Nola', 'Nolan', 'Nora', 'Norah', 'Norbert', 'Noreen',
                 'Norma', 'Norman', 'Nova', 'Nyla', 'Oakes', 'Oakley', 'Oasis', 'Ocean', 'Octavia', 'Octavio', 'Odalis',
                 'Odalys', 'Odele', 'Odelia', 'Odette', 'Oisin', 'Olaf', 'Olga', 'Oli', 'Olive', 'Oliver', 'Olivia',
                 'Ollie', 'Olly', 'Omar', 'Oona', 'Oonagh', 'Opal', 'Ophelia', 'Oprah', 'Oran', 'Oriana', 'Orianna',
                 'Orion', 'Orla', 'Orlaith', 'Orlando', 'Orson', 'Oscar', 'Osvaldo', 'Oswald', 'Otis', 'Otto', 'Owen',
                 'Ozzie', 'Ozzy', 'Pablo', 'Paco', 'Paddy', 'Padraig', 'Page', 'Paige', 'Paisley', 'Palmer', 'Paloma',
                 'Pam', 'Pamela', 'Pandora', 'Pansy', 'Paola', 'Paolo', 'Paris', 'Parker', 'Pascal', 'Pat', 'Patience',
                 'Patrice', 'Patricia', 'Patrick', 'Patsy', 'Patti', 'Patty', 'Paul', 'Paula', 'Paulette', 'Paulina',
                 'Pauline', 'Paxton', 'Payton', 'Payton', 'Peace', 'Pearce', 'Pearl', 'Pedro', 'Peggy', 'Penelope',
                 'Penny', 'Percy', 'Perla', 'Perrie', 'Perry', 'Persephone', 'Petar', 'Pete', 'Peter', 'Petra',
                 'Petunia', 'Peyton', 'Peyton', 'Phebian', 'Phil', 'Philip', 'Philippe', 'Phillip', 'Phillipa',
                 'Philomena', 'Phineas', 'Phoebe', 'Phoenix', 'Phoenix', 'Phyllis', 'Pierce', 'Piers', 'Pip', 'Piper',
                 'Pippa', 'Pixie', 'Polly', 'Pollyanna', 'Poppy', 'Porter', 'Portia', 'Poul', 'Prakash', 'Precious',
                 'Presley', 'Preslie', 'Preston', 'Primrose', 'Prince', 'Princess', 'Princeton', 'Priscilla', 'Priya',
                 'Promise', 'Prudence', 'Prue', 'Queenie', 'Quentin', 'Quiana', 'Quincy', 'Quinlan', 'Quinn', 'Quinn',
                 'Quinton', 'Quintrell', 'Rabia', 'Rachael', 'Rachel', 'Rachelle', 'Rae', 'Raegan', 'Raelyn', 'Rafael',
                 'Rafferty', 'Raheem', 'Rahul', 'Raiden', 'Raina', 'Raine', 'Raj', 'Rajesh', 'Ralph', 'Ram', 'Rameel',
                 'Ramon', 'Ramona', 'Ramsey', 'Ramsha', 'Randal', 'Randall', 'Randi', 'Randolph', 'Randy', 'Rani',
                 'Rania', 'Raoul', 'Raphael', 'Raquel', 'Rashad', 'Rashan', 'Rashid', 'Raul', 'Raven', 'Ravi', 'Ray',
                 'Raya', 'Raylan', 'Raymond', 'Rayna', 'Rayne', 'Reagan', 'Reanna', 'Reanne', 'Rebecca', 'Rebekah',
                 'Reece', 'Reed', 'Reef', 'Reese', 'Reese', 'Regan', 'Reggie', 'Regina', 'Reginald', 'Rehan', 'Reid',
                 'Reilly', 'Reilly', 'Reina', 'Remco', 'Remi', 'Remington', 'Remy', 'Ren', 'Rena', 'Renata', 'Rene',
                 'Rene', 'Renee', 'Renesmee', 'Reuben', 'Rex', 'Reyna', 'Reynaldo', 'Reza', 'Rhea', 'Rhett', 'Rhian',
                 'Rhianna', 'Rhiannon', 'Rhoda', 'Rhona', 'Rhonda', 'Rhys', 'Ria', 'Rian', 'Rianna', 'Ricardo', 'Rich',
                 'Richard', 'Richie', 'Rick', 'Rickey', 'Ricki', 'Rickie', 'Ricky', 'Rico', 'Rider', 'Rihanna', 'Rik',
                 'Riker', 'Rikki', 'Riley', 'Riley', 'Rio', 'Rita', 'River', 'River', 'Riya', 'Roan', 'Roanne', 'Rob',
                 'Robbie', 'Robby', 'Robert', 'Roberta', 'Roberto', 'Robin', 'Robin', 'Robyn', 'Rocco', 'Rochelle',
                 'Rocio', 'Rock', 'Rocky', 'Rod', 'Roderick', 'Rodger', 'Rodney', 'Rodolfo', 'Rodrigo', 'Rogelio',
                 'Roger', 'Rohan', 'Roisin', 'Roland', 'Rolanda', 'Rolando', 'Roman', 'Romeo', 'Ron', 'Ronald', 'Ronan',
                 'Ronda', 'Roni', 'Ronnie', 'Ronny', 'Roosevelt', 'Rory', 'Rosa', 'Rosalie', 'Rosalina', 'Rosalind',
                 'Rosalinda', 'Rosalynn', 'Rosanna', 'Roscoe', 'Rose', 'Roseanne', 'Rosella', 'Rosemarie', 'Rosemary',
                 'Rosetta', 'Rosie', 'Ross', 'Rosy', 'Rowan', 'Rowan', 'Rowena', 'Roxana', 'Roxanne', 'Roxie', 'Roxy',
                 'Roy', 'Royce', 'Rozlynn', 'Ruairi', 'Ruben', 'Rubin', 'Ruby', 'Rudolph', 'Rudy', 'Rue', 'Rufus',
                 'Rupert', 'Russ', 'Russell', 'Rusty', 'Ruth', 'Ruthie', 'Ryan', 'Ryanne', 'Rydel', 'Ryder', 'Ryker',
                 'Rylan', 'Ryland', 'Rylee', 'Ryleigh', 'Ryley', 'Rylie', 'Sabina', 'Sabine', 'Sable', 'Sabrina',
                 'Sacha', 'Sade', 'Sadhbh', 'Sadie', 'Saffron', 'Safire', 'Safiya', 'Sage', 'Sahara', 'Said', 'Saige',
                 'Saira', 'Sally', 'Salma', 'Salome', 'Salvador', 'Salvatore', 'Sam', 'Sam', 'Samantha', 'Samara',
                 'Samia', 'Samir', 'Samira', 'Sammie', 'Sammy', 'Sammy', 'Samson', 'Samuel', 'Sandeep', 'Sandra',
                 'Sandy', 'Sandy', 'Sania', 'Sanjay', 'Santiago', 'Saoirse', 'Sapphire', 'Sara', 'Sarah', 'Sarina',
                 'Sariya', 'Sascha', 'Sasha', 'Sasha', 'Saskia', 'Saul', 'Savanna', 'Savannah', 'Sawyer', 'Scarlet',
                 'Scarlett', 'Scot', 'Scott', 'Scottie', 'Scotty', 'Seamus', 'Sean', 'Seb', 'Sebastian', 'Sebastianne',
                 'Sebastien', 'Sebestian', 'Selah', 'Selena', 'Selene', 'Selina', 'Selma', 'Senuri', 'September',
                 'Seren', 'Serena', 'Serenity', 'Sergio', 'Seth', 'Shadrach', 'Shakira', 'Shana', 'Shane', 'Shania',
                 'Shannon', 'Shannon', 'Shari', 'Sharon', 'Shary', 'Shaun', 'Shauna', 'Shawn', 'Shawn', 'Shawna',
                 'Shawnette', 'Shay', 'Shayla', 'Shayna', 'Shayne', 'Shea', 'Shea', 'Sheba', 'Sheena', 'Sheila',
                 'Shelby', 'Sheldon', 'Shelia', 'Shelley', 'Shelly', 'Shelton', 'Sheri', 'Sheridan', 'Sherlock',
                 'Sherman', 'Sherri', 'Sherrie', 'Sherry', 'Sheryl', 'Shiloh', 'Shirley', 'Shivani', 'Shona', 'Shonagh',
                 'Shreya', 'Shyla', 'Sian', 'Sid', 'Sidney', 'Sidney', 'Sienna', 'Sierra', 'Sigourney', 'Silas',
                 'Silvia', 'Simeon', 'Simon', 'Simone', 'Simran', 'Sinead', 'Siobhan', 'Sky', 'Sky', 'Skye', 'Skylar',
                 'Skylar', 'Skyler', 'Skyler', 'Slade', 'Sloane', 'Snow', 'Sofia', 'Sofie', 'Sol', 'Solomon', 'Sondra',
                 'Sonia', 'Sonja', 'Sonny', 'Sonya', 'Sophia', 'Sophie', 'Sophy', 'Soren', 'Sorrel', 'Spencer', 'Spike',
                 'Spring', 'Stacey', 'Stacey', 'Staci', 'Stacie', 'Stacy', 'Stacy', 'Stan', 'Stanley', 'Star', 'Starla',
                 'Stefan', 'Stefanie', 'Stella', 'Steph', 'Stephan', 'Stephanie', 'Stephen', 'Sterling', 'Steve',
                 'Steven', 'Stevie', 'Stewart', 'Stone', 'Storm', 'Stuart', 'Sue', 'Sufyan', 'Sugar', 'Suki',
                 'Sullivan', 'Summer', 'Susan', 'Susanna', 'Susannah', 'Susanne', 'Susie', 'Sutton', 'Suzanna',
                 'Suzanne', 'Suzette', 'Suzie', 'Suzy', 'Sven', 'Sybil', 'Sydney', 'Sylvester', 'Sylvia', 'Sylvie',
                 'Tabatha', 'Tabitha', 'Tadhg', 'Tahlia', 'Tala', 'Talia', 'Talitha', 'Taliyah', 'Tallulah', 'Talon',
                 'Tam', 'Tamara', 'Tamera', 'Tami', 'Tamia', 'Tamika', 'Tammi', 'Tammie', 'Tammy', 'Tamra', 'Tamsin',
                 'Tania', 'Tanika', 'Tanisha', 'Tanner', 'Tanya', 'Tara', 'Tariq', 'Tarquin', 'Taryn', 'Tasha',
                 'Tasmin', 'Tate', 'Tatiana', 'Tatum', 'Tawana', 'Taya', 'Tayah', 'Tayla', 'Taylah', 'Tayler', 'Taylor',
                 'Taylor', 'Teagan', 'Ted', 'Teddy', 'Teegan', 'Tegan', 'Teigan', 'Tenille', 'Teo', 'Terence', 'Teresa',
                 'Teri', 'Terrance', 'Terrell', 'Terrence', 'Terri', 'Terrie', 'Terry', 'Terry', 'Tess', 'Tessa',
                 'Tevin', 'Tex', 'Thad', 'Thaddeus', 'Thalia', 'Thea', 'Thelma', 'Theo', 'Theodora', 'Theodore',
                 'Theophilus', 'Theresa', 'Therese', 'Thomas', 'Thomasina', 'Thor', 'Tia', 'Tiago', 'Tiana', 'Tiberius',
                 'Tiegan', 'Tiffany', 'Tiger', 'Tilly', 'Tim', 'Timmy', 'Timothy', 'Tina', 'Tisha', 'Tito', 'Titus',
                 'Tobias', 'Tobin', 'Toby', 'Tod', 'Todd', 'Tom', 'Tomas', 'Tommie', 'Tommy', 'Toni', 'Tonia', 'Tony',
                 'Tonya', 'Tori', 'Torin', 'Toryn', 'Trace', 'Tracey', 'Tracey', 'Traci', 'Tracie', 'Tracy', 'Tracy',
                 'Travis', 'Tray', 'Tremaine', 'Trent', 'Trenton', 'Trevon', 'Trevor', 'Trey', 'Tricia', 'Trina',
                 'Trinity', 'Trish', 'Trisha', 'Trista', 'Tristan', 'Tristen', 'Triston', 'Trixie', 'Trixy', 'Troy',
                 'Trudy', 'Truman', 'Tucker', 'Tula', 'Tulip', 'Ty', 'Tyler', 'Tyra', 'Tyrese', 'Tyrone', 'Tyson',
                 'Ulrica', 'Ulysses', 'Uma', 'Umar', 'Una', 'Uriah', 'Uriel', 'Ursula', 'Usama', 'Valentin',
                 'Valentina', 'Valentine', 'Valentino', 'Valeria', 'Valerie', 'Valery', 'Van', 'Vance', 'Vanessa',
                 'Vasco', 'Vaughn', 'Veda', 'Velma', 'Venetia', 'Venus', 'Vera', 'Verity', 'Vernon', 'Veronica',
                 'Vicki', 'Vickie', 'Vicky', 'Victor', 'Victoria', 'Vienna', 'Vihan', 'Vijay', 'Vikram', 'Vince',
                 'Vincent', 'Vinnie', 'Viola', 'Violet', 'Violetta', 'Virgil', 'Virginia', 'Vishal', 'Vivian', 'Vivian',
                 'Viviana', 'Vivien', 'Vivienne', 'Vlad', 'Vladimir', 'Wade', 'Walker', 'Wallace', 'Wallis', 'Walter',
                 'Wanda', 'Warren', 'Waverley', 'Waylon', 'Wayne', 'Wendell', 'Wendi', 'Wendy', 'Wes', 'Wesley',
                 'Weston', 'Whitney', 'Wilbert', 'Wilbur', 'Wiley', 'Wilfred', 'Wilhelm', 'Wilhelmina', 'Will', 'Willa',
                 'Willam', 'Willard', 'Willem', 'William', 'Willie', 'Willis', 'Willow', 'Wilma', 'Wilson', 'Winnie',
                 'Winnifred', 'Winona', 'Winston', 'Winter', 'Wolfgang', 'Woody', 'Wyatt', 'Xander', 'Xandra', 'Xanthe',
                 'Xavier', 'Xaviera', 'Xena', 'Xerxes', 'Xia', 'Ximena', 'Xochil', 'Xochitl', 'Yahir', 'Yardley',
                 'Yasmin', 'Yasmine', 'Yazmin', 'Yehudi', 'Yelena', 'Yesenia', 'Yestin', 'Yolanda', 'York', 'Ysabel',
                 'Yulissa', 'Yuri', 'Yusuf', 'Yvaine', 'Yves', 'Yvette', 'Yvonne', 'Zac', 'Zach', 'Zachariah',
                 'Zachary', 'Zachery', 'Zack', 'Zackary', 'Zackery', 'Zada', 'Zaheera', 'Zahra', 'Zaiden', 'Zain',
                 'Zaine', 'Zaira', 'Zak', 'Zakia', 'Zali', 'Zander', 'Zane', 'Zara', 'Zaria', 'Zaya', 'Zayden', 'Zayla',
                 'Zayn', 'Zayne', 'Zeb', 'Zebulon', 'Zed', 'Zeke', 'Zelda', 'Zelida', 'Zelina', 'Zena', 'Zendaya',
                 'Zeph', 'Zia', 'Ziggy', 'Zina', 'Zion', 'Ziva', 'Zoe', 'Zoey', 'Zola', 'Zoltan', 'Zora', 'Zoya',
                 'Zula', 'Zuri', 'Zuriel', 'Zyana', 'Zylen']
    return "%s.%s.%s.%s" % (
        chr(random.randint(65, 90)), eng_names[random.randint(0, len(eng_names) - 1)], chr(random.randint(65, 90)),
        chr(random.randint(65, 90)))
    # a = random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 8)
    # code = ""
    # code = code.join(a)
    # return code


def result(stu_phone, tea_phone):
    """
    组装返回结果
    :param stu_phone:
    :param tea_phone:
    :return:
    """
    list = []
    stu_info = '学生账户：' + str(stu_phone)
    tea_info = ' 老师账户：' + str(tea_phone) + ' 密码都默认为123456'
    list.append(stu_info)
    list.append(tea_info)
    return list


# 请求失败时返回
class NoSuccessExceptin(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return (self.msg)


# 字节转字典
def bytes_to_dict(data):
    if isinstance(data, bytes):
        return json.loads(bytes.decode(data))
    else:
        return {}


# 组装返回数据结构
def response_data(data, status, msg):
    return dict(data=data, meta=status, msg=msg)


# 返回字典数据
def dict_data(ret=1, data='', msg=''):
    return dict(ret=ret, data=data, msg=msg)


# 数据库操作，能力提升课用
class Database:
    def __init__(self):
        self.conn = pymysql.connect(
            host='10.106.68.1',
            port=4000,
            user='product',
            password='banyu2017@TESTMYSQL',
            database='curriculum',
            autocommit=True
        )

    def query(self, sql):
        cursor = self.conn.cursor()
        print("Query: ", sql)
        cursor.execute(sql)
        return cursor.fetchall()

    def purge(self, stuid):
        self.query('delete from curriculum_record_lesson_schedule where stuid = %d' % stuid)
        self.query('delete from curriculum_record_lesson_student_booking_info where stuid = %d' % stuid)


def date_to_stamp(date):
    """
    字符串类型时间"2019-4-13 10:02:23"转时间戳
    :param date:
    :return:
    """
    # 转为时间数组
    timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def get_lesson_kid(type):
    """
    根据课程类型获取kid
    :param type:
    <el-radio :label="0">欧美官方课</el-radio>
    <el-radio :label="1">欧美真人试听课</el-radio>
    <el-radio :label="2">菲教官方课</el-radio>
    <el-radio :label="3">菲教真人试听课</el-radio>
    <el-radio :label="4">欧美AI试听课</el-radio>
    <el-radio :label="5">菲教AI试听课</el-radio>
    <el-radio :label="6">欧美启蒙课</el-radio>
    <el-radio :label="7">菲教启蒙课</el-radio>
    <el-radio :label="8">中教AI试听课</el-radio>

    :return:
    """
    if int(type) == 0:  # 0 欧美官方课
        kid = KIDS.get('EURO_OFFICIAL_KID')
    elif int(type) == 1 or int(type) == 4 or int(type) == 8:  # 欧美试听课
        kid = KIDS.get('EURO_AUDITION_KID')
    elif int(type) == 2:  # 菲教官方课
        kid = KIDS.get('PH_OFFICIAL_KID')
    elif int(type) == 3 or int(type) == 5:  # 菲教试听课
        kid = KIDS.get('PH_AUDITION_KID')
    elif int(type) == 6:
        kid = KIDS.get('EURO_INITIATION_KID')
    elif int(type) == 7:
        kid = KIDS.get('PH_INITIATION_KID')
    else:
        kid = 0
    return kid


def get_current_zero_times():
    today = datetime.date.today()
    zore_times = int(time.mktime(today.timetuple()))
    return zore_times


def genera_login_token():
    return uuid.uuid4().hex


def jump_util(stu_id, tea_id, str_stamp, stulates, studuations, teaduations, tealates, kid, isaiclass):
    """
    :param stu_id: 学生id
    :param tea_id: 老师id
    :param str_stamp: 跳课时间
    :param stulates: 学生迟到时间，单位s
    :param studuations: 学生出席时间
    :param teaduations: 老师出席时间
    :param tealates: 老师迟到时间
    :param kid: 课程id
    :param isaiclass: 是否为AI课
    :return:
    """
    return "ssh 10.111.131.212 /data/home/super/mwd/jump_class  -stuid " + str(stu_id) + " -teaid " + str(
        tea_id) + " -stampstr " + str(str_stamp) + " -stulates " + str(stulates) + " -studuations " + str(
        studuations) + " -teaduations " + \
           str(teaduations) + " -tealates " + str(tealates) + " -kid " + str(
        kid) + " -isaiclass " + str(
        isaiclass)


def change_rt(stu_id, ct, rt_stamp):
    # ssh 10.111.131.212 /data/home/super/mwd/uptime -uidstr 2865458380 -ct 1624954831 -rt 1622476800
    command = "ssh 10.111.131.212 /data/home/super/mwd/uptime -uidstr {} -ct {} -rt {}".format(stu_id, ct, rt_stamp)
    return command


# 获取文件的md5
def md5_file(name):
    m = hashlib.md5()
    a_file = open(name, 'rb')  # 需要使用二进制格式读取文件内容
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()


def login_check(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('login_status'):
            return JsonResponse({'ret': 99, 'msg': 'session invalid'})
        return func(request, *args, **kwargs)

    return wrapper
#非分页查询返回数据
def json_response(res, errcode, errmsg):
    if res is None:
        data = {
            "errcode": errcode,
            "errmsg": errmsg,
        }
    else:
        data = {
            "errcode": errcode,
            "errmsg": errmsg,
            "data": res
        }
    return JsonResponse(data, safe=False)

# 自动生成创建时间和更新时间
def deal_logic_dict(logic_dict, type="add"):
    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    ts = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    logic_dict['update_time'] = ts
    if type == 'add':
        logic_dict['create_time'] = ts
    return logic_dict

# id生成器
def get_itme_id():
    itme_id = str(int(time.time() * 1000)) + str(int(time.perf_counter() * 1000000))
    return str(itme_id)
def deal_model_id(logic_dict, id_name):
    _id = logic_dict.get(id_name, None)
    if not _id:
        logic_dict.setdefault(id_name, get_itme_id())
    return logic_dict

def get_file_base_dir():
    try:
        file_root_path = None
    except:
        file_root_path = None
    if not file_root_path or len(file_root_path) == 0:
        return os.getcwd()
    else:
        return file_root_path