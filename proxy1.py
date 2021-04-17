class College:
    'Resource-intensive object'
    def studyingInCollege(self):
        print('Studying In College...')

class CollegeProxy:
    def __init__(self):
        self.feeBalance = 100
        self.college = None 
    def studyingInCollege(self):
        print('Proxy in action. Checking to see if the balance of student is clear or not...')                
        if self.feeBalance <= 500:
            # If the balance is less than 500, let him study.
            self.college = College() 
            self.college.studyingInCollege() 
        else:
            # Otherwise, don't instantiate the college object.
            print('Your fee balance is greater than 500, first pay the fee')

'main method'            
