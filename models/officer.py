class Officer:
    def __init__(self,officer_id,name,rank,station,case_assigned,cases_solved,case_pending,contact_number):
        self.officer_id=officer_id
        self.name=name
        self.rank=rank
        self.station=station
        self.case_assigned=case_assigned
        self.cases_solved=cases_solved
        self.case_pending=case_pending
        self.contact_number=contact_number

    def to_dict(self):
        return {
            "officer_id":self.officer_id,
            "Name":self.name,
            "Rank":self.rank,
            "Station":self.station,
            "Case Assigned":self.case_assigned,
            "Case Solved" :self.cases_solved,
            "Case Pending":self.case_pending,
            "Contact Number":self.contact_number
        }






