class Member():
	def __init__(self, full_name=[]):
		self.full_name = [] 

	def introduction(self):
		name = input('Name of attendee: ')
		self.full_name.append(name)
		print(f'Welcome {self.full_name}')

member = Member()
member.introduction()
################################################################
class Student():
	def __init__(self, reason=[]):
		self.reason = []
	
	def reason_for_coming(self):
			reasoning = input('Why would you like to attend the number one school, CodeBar?')
			self.reason.append(reasoning)
			print(f'{self.reason}')

new_person = Student()
new_person.reason_for_coming()
# print(f'Welcome {member.full_name}! You said you wanted to attend because, {new_person.reason}')
##############################################################
class Instructor():
	def __init__(self, bio=[], skills=[], add_skill=[]):
		self.bio = []
		self.skills = []
		self.add_skill = []
	
	def instructor_info(self):
		bio_info = input('Tell us a little about yourself.')
		skill_info = input('What skills do you have?')
		add_a_skill = input('Add a skill you want to learn...')
		self.bio.append(bio_info)
		self.skills.append(skill_info)
		self.add_skill.append(add_a_skill)

prof_genius = Instructor()
prof_genius.instructor_info()
# print(f'Welcome {member.full_name}! You said you wanted to attend because, {new_person.reason}. Here are some of the things you wrote about yourself...{prof_genius.bio} and you are skilled at {prof_genius.skills} but want to learn {prof_genius.add_skill}.')
################################################################################

class Work_shop():
	def __init__(self, date=[], subject=[], instructors=0, students=0):
		self.date = date
		self.subject = subject
		self.instructors = 0
		self.students = 0
	def add_participant(self, new_student=''):
		answer = input('Are you a student or instructor?')
		if answer == 'instructors':
			self.instructors += 1 
		else: self.students += 1 
		the_date = input('When would you like to attend?')
		the_subject = input('What subject would you like to study?')
		self.date.append(the_date)
		self.subject.append(the_subject)


new_workshop = Work_shop()
new_workshop.add_participant()

print(f'Welcome {member.full_name}! You said you wanted to attend because, {new_person.reason}. Here are some of the things you wrote about yourself...{prof_genius.bio} and you are skilled at {prof_genius.skills} but want to learn {prof_genius.add_skill}. You signed up for {new_workshop.subject} event on {new_workshop.date}. {new_workshop.students} student will be there and {new_workshop.instructors} instructors will attend.')


















