from priority_queue import PriorityQueue
import matplotlib.pyplot as plt

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
        self.patient_counts = []

    def admit_patient(self, patient):
        try:
            if not isinstance(patient, Patient):
                raise ValueError("Invalid patient object.")
            
            if not isinstance(patient.priority, int) or patient.priority <= 0:
                raise ValueError("Priority must be a positive integer.")
            
            print(f"Admitting {patient} to the emergency room.")
            self.queue.push(patient, patient.priority)
        except ValueError as e:
            print(f"Error: {e}")

    def treat_patient(self):
        if not self.queue.heap:
            print("No patients to treat.")
            return

        patient = self.queue.pop()
        print(f"Treating {patient}.")
        self.patient_counts.append(len(self.queue.heap) + 1)
        return patient

    def visualize_patient_flow(self):
        plt.plot(range(len(self.patient_counts)), self.patient_counts, marker='o')
        plt.xlabel('Time Intervals')
        plt.ylabel('Number of Patients')
        plt.title('Patient Flow in Emergency Room')
        plt.show()

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

    er.visualize_patient_flow()
