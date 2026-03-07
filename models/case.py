class Case:
    def __init__(self, case_id, title, desc, status, assigned_officer, date_created):
        self.case_id=case_id
        self.title=title
        self.desc=desc
        self.status=status
        self.assigned_officer=assigned_officer
        self.date_created=date_created

    def to_dict(self):
        return{
            "Case_id":self.case_id,
            "Title":self.title,
            "Assigned_officer":self.assigned_officer,
            "Description":self.desc,
            "Status":self.status,
            "Date_created":self.date_created
        }