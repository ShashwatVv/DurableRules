# -*- coding: utf-8 -*-
"""AI3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/182eR74xYyZFvYkD99ajHLR19JiNEq6Tb
"""

pip install durable-rules

# Durable Module implementing Forward Chaining.
# Task:- Course and extra-curricular activity suggestion based upon grades and interests.
# Created by - Shashwat Vaibhav, MT21082

from durable.lang import *

# considering three major factors while making suggestions:
# 1.Interest
# 2.Hobby
# 3.Overall Grade('A', 'B' or 'C'). three grades in order of excellent, moderate and below-par

with ruleset('interest'):
  #choice 1---> Cyber Security
  @when_all((m.choice=='Cyber-Security')&(m.grade=='A'))
  def fun1(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ADVANCED Network Security'})
  
  @when_all((m.choice=='Cyber-Security')&(m.grade=='A'))
  def fun1(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ADVANCED Network Security'})

  @when_all((m.choice=='Cyber-Security')&(m.grade=='A'))
  def fun1(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ADVANCED Network Security'})

  @when_all((m.choice=='Cyber-Security')&(m.grade=='B'))
  def fun1(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Cryptography and Network Security'})

  @when_all((m.choice=='Cyber-Security')&(m.grade=='B'))
  def fun1(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Cryptography and Network Security'})
  
  @when_all((m.choice=='Cyber-Security')&(m.grade=='B'))
  def fun1(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Cryptography and Network Security'})

  @when_all((m.choice=='Cyber-Security')&(m.grade=='C'))
  def fun1(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Introduction to Network Administration'})

  @when_all((m.choice=='Cyber-Security')&(m.grade=='C'))
  def fun1(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Introduction to Network Administration'})
  
  @when_all((m.choice=='Cyber-Security')&(m.grade=='C'))
  def fun1(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Introduction to Network Administration'})


  #choice 2--> Artificial Intelligence

  @when_all((m.choice=='Artificial Intelligence')&(m.grade=='A'))
  def fun2(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ADVANCED Statistical Learning'})
  
  @when_all((m.choice=='Artificial Intelligence')&(m.grade=='A'))
  def fun2(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ADVANCED Statistical Learning'})

  @when_all((m.choice=='Artificial Intelligence')&(m.grade=='A'))
  def fun2(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ADVANCED Statistical Learning'})

  @when_all((m.choice=='Artificial Intelligence')&(m.grade=='B'))
  def fun2(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Computer Vision'})

  @when_all((m.choice=='Artificial Intelligence')&(m.grade=='B'))
  def fun2(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Computer Vision'})
  
  @when_all((m.choice=='Artificial Intelligence')&(m.grade=='B'))
  def fun2(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Computer Vision'})

  @when_all((m.choice=='Artificial Intelligence')&(m.grade=='C'))
  def fun2(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Introduction to NLP'})

  @when_all((m.choice=='Artificial Intelligence')&(m.grade=='C'))
  def fun2(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Introduction to NLP'})
  
  @when_all((m.choice=='Artificial Intelligence')&(m.grade=='C'))
  def fun2(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Introduction to NLP'})

  #Choice 3--> Bio Informatics
  @when_all((m.choice=='Bio Informatics')&(m.grade=='A'))
  def fun3(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ML in BioMedical Applications'})

  @when_all((m.choice=='Bio Informatics')&(m.grade=='A'))
  def fun3(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ML in BioMedical Applications'})
  
  @when_all((m.choice=='Bio Informatics')&(m.grade=='A'))
  def fun3(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ML in BioMedical Applications'})

  @when_all((m.choice=='Bio Informatics')&(m.grade=='B'))
  def fun3(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Computational Gastronomy'})

  @when_all((m.choice=='Bio Informatics')&(m.grade=='B'))
  def fun3(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Computational Gastronomy'})
  
  @when_all((m.choice=='Bio Informatics')&(m.grade=='B'))
  def fun3(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Computational Gastronomy'})
  
  @when_all((m.choice=='Bio Informatics')&(m.grade=='C'))
  def fun3(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Advanced R/Python for CB'})

  @when_all((m.choice=='Bio Informatics')&(m.grade=='C'))
  def fun3(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Advanced R/Python for CB'})
  
  @when_all((m.choice=='Bio Informatics')&(m.grade=='C'))
  def fun3(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Advanced R/Python for CB'})

  #Choice 4--> Mobile Computing
  @when_all((m.choice=='Mobile Computing')&(m.grade=='A'))
  def fun4(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ADVANCED Wireless Design'})

  @when_all((m.choice=='Mobile Computing')&(m.grade=='A'))
  def fun4(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ADVANCED Wireless Design'})
  
  @when_all((m.choice=='Mobile Computing')&(m.grade=='A'))
  def fun4(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'ADVANCED Wireless Design'})

  @when_all((m.choice=='Mobile Computing')&(m.grade=='B'))
  def fun4(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Network Topology'})

  @when_all((m.choice=='Mobile Computing')&(m.grade=='B'))
  def fun4(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Network Topology'})
  
  @when_all((m.choice=='Mobile Computing')&(m.grade=='B'))
  def fun4(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Network Topology'})
  
  @when_all((m.choice=='Mobile Computing')&(m.grade=='C'))
  def fun4(obj):
    obj.assert_fact('hobby',{'area':'music'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Cloud Computing'})

  @when_all((m.choice=='Mobile Computing')&(m.grade=='C'))
  def fun4(obj):
    obj.assert_fact('hobby',{'area':'sports'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Cloud Computing'})
  
  @when_all((m.choice=='Mobile Computing')&(m.grade=='C'))
  def fun4(obj):
    obj.assert_fact('hobby',{'area':'writing'})
    obj.assert_fact({'subject':'Opt for','predicate':'course name', 'object': 'Cloud Computing'})

  @when_all(+m.subject)
  def show(obj):
    print('Fact/Statement: {0} {1} {2}'.format(obj.m.subject, obj.m.predicate, obj.m.object))

#Let the clubs and associated activities be as follows:
#1. Sur Sangam - vocals and instrumentals training as well as live performance.
#2. Krida Mandal - Sports facility for cricket, footbal, squash and others.
#3. Lekhani - Magazine writing, poetry, story-telling/writing, journalism, etc.

with ruleset('hobby'):
  @when_all(m.area=='music')
  def fun4(hobj):
    hobj.assert_fact({'subject':'Join the SUR SANGAM club and feel the note within!!'})

  @when_all(m.area=='sports')
  def fun4(hobj):
    hobj.assert_fact({'subject':'Wake up the Ronaldo and Sachin within you, Join the KRIDA MANDAL CLUB!!'})

  @when_all(m.area=='writing')
  def fun4(hobj):
    hobj.assert_fact({'subject':'Are you the next SARTRE, or the next DINNKAR, Join the LEKHANI CLUB!!'})

  @when_all(+m.subject)
  def show(hobj):
    print('Fact/Statement: {0}'.format(hobj.m.subject))

## Asserting Fact:
#assert_fact('interest',{'choice':'choice name', 'grade':'A B or C'})

assert_fact('interest',{'choice':'Mobile Computing', 'grade':'A'})

