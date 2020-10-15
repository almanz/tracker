def main():
    print("in main()")
    data = [("NoseCone Technologies Inc.","yes","https://www.thesmartcone.com/",
            "Experienced Software Engineer","https://ca.indeed.com/viewjob?jk=ae2a14acdc7258ba",
            None,None),("Hatchways","yes","https://ca.indeed.com/viewjob?jk=c71fd8608152d5d3","Jr. Software Developer","none","none")]
    # data = ("o","o","o","o","o","o","o")
    tracker = JobTracker.JobTracker()
    tracker.addjob(data)
    print("added job.")
    tracker.to_file()
    print("converted to JSON.")
    print("argv arguments:",sys.argv[0])
    print("names in namespace:",dir())
    print("done!")
    return 0


if __name__ == "__main__":
    import JobTracker
    import sys
    main()