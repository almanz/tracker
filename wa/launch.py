import JobTracker
import sys

def main():
    print("in main()")
    data = [("NoseCone Technologies Inc.","yes","https://www.thesmartcone.com/",
            "Experienced Software Engineer","https://ca.indeed.com/viewjob?jk=ae2a14acdc7258ba",
            None,None),("Hatchways","yes","https://ca.indeed.com/viewjob?jk=c71fd8608152d5d3","Jr. Software Developer","none","none")]
    tracker = JobTracker.JobTracker()
    tracker.addjob(data)
    print("added job.")
    tracker.to_json()
    print("converted to JSON.")
    print("argv arguments:",sys.argv[0])
    print("done!")
    return 0


if __name__ == "__main__":
    main()