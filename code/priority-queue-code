class Patient:
    def __init__(self, name, condition, priority):
        self.name = name
        self.condition = condition
        self.priority = priority

    def __str__(self):
        return f"{self.name} ({self.condition})"


class EmergencyRoom:
    def __init__(self):
        self.queue = PriorityQueue()

    def admit_patient(self, patient):
        print(f"Admitting {patient} to the emergency room.")
        self.queue.push(patient, patient.priority)

    def treat_patient(self):
        if not self.queue.heap:
            print("No patients to treat.")
            return

        patient = self.queue.pop()
        print(f"Treating {patient}.")
        return patient


if __name__ == "__main__":
    er = EmergencyRoom()

    patient1 = Patient("John", "Critical condition", 1)
    patient2 = Patient("Alice", "Severe injury", 2)
    patient3 = Patient("Bob", "Broken arm", 3)

    er.admit_patient(patient1)
    er.admit_patient(patient2)
    er.admit_patient(patient3)

    treated_patient = er.treat_patient()
    print(f"Treated: {treated_patient}")

    treated_patient = er.treat_patient()
    print(f"Treated: {treated_patient}")

    treated_patient = er.treat_patient()
    print(f"Treated: {treated_patient}")
