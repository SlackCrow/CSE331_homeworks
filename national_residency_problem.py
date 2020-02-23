from Match import Match
from collections import defaultdict
import random

class Solution:
    
    def __init__(self, m, n, hospital_list, student_list, hosp_open_slots):
        """
            The constructor exists only to initialize variables. You do not need to change it.
            :param m: The number of hospitals
            :param n: The number of students
            :param hospital_list: The preference list of hospitals, as a dictionary.
            :param student_list: The preference list of the students, as a dictionary.
            :param hosp_open_slots: Open slots of each hospital
            """
        self.m = m
        self.n = n
        self.hospital_list = hospital_list
        self.student_list = student_list
        self.hosp_open_slots = hosp_open_slots
        self.alreadyProposed = dict()
        self.matchedStudent = dict()
        self.matchedHospital = defaultdict(list)
        self.listToReturn = list()
    
    def get_matches(self):
        while self.hosp_open_slots:
            hospital = random.choice(list(self.hosp_open_slots.keys()))
            preferredStudent = self.getPreferredStudent(hospital)
            if self.isStudentFree(preferredStudent):
                self.addMatch(preferredStudent,hospital)
            else:
                if self.checkPreferred(hospital,preferredStudent):
                    self.freeMatch(preferredStudent)
                    self.addMatch(preferredStudent,hospital)
                else:
                    self.rejectedRecordUpdate(hospital,preferredStudent)
        for key, value in self.matchedHospital.items():
            if(len(value) == 1):
                self.listToReturn.append((key,value[0]))
            else:
                for element in value:
                    self.listToReturn.append((key,element))
        return self.listToReturn
            
    def getPreferredStudent(self,hospital):
            for student in self.hospital_list[hospital]:
                if hospital in self.alreadyProposed:
                    if student in self.alreadyProposed[hospital]:
                        pass
                    else:
                        return student
                else:
                    return self.hospital_list[hospital][0]

    def isStudentFree(self,student):
        if student in self.matchedStudent:
            return False
        else:
            return True

    def checkPreferred(self,hospital,student):
        originalHospital = self.matchedStudent[student]
        originalHospitalIndex = self.student_list[student].index(originalHospital)
        newHospitalIndex = self.student_list[student].index(hospital)
        if newHospitalIndex < originalHospitalIndex:
            return True
        else:
            return False
    
    def freeMatch(self, student):
        hospitalToFree = self.matchedStudent[student]
        for output in self.matchedHospital.pop(hospitalToFree):
            if output == student:
                pass
            else:
                self.matchedHospital[hospitalToFree].append(output)
        if hospitalToFree in self.hosp_open_slots:
            self.hosp_open_slots[hospitalToFree] = self.hosp_open_slots[hospitalToFree]+1
        else:
            self.hosp_open_slots[hospitalToFree] = 1
        self.rejectedRecordUpdate(hospitalToFree,student)

    def addMatch(self, student, hospital):
        self.matchedHospital[hospital].append(student)
        self.matchedStudent[student] = hospital
        if(self.hosp_open_slots[hospital] == 1):
            self.hosp_open_slots.pop(hospital)
        else:
            self.hosp_open_slots[hospital] = self.hosp_open_slots[hospital]-1

    def rejectedRecordUpdate(self,hospital,preferredStudent):
        if hospital in self.alreadyProposed:
            self.alreadyProposed[hospital].append(preferredStudent)
        else:
            listToAdd = []
            listToAdd.append(preferredStudent)
            self.alreadyProposed[hospital] = listToAdd