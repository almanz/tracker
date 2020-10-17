def main():
    print("in main()")
    file = sys.argv[1:]
    print(len(sys.argv))
    if(len(sys.argv)==1):
        data = [("NoseCone Technologies Inc.","yes","https://www.thesmartcone.com/",
        "Experienced Software Engineer","https://ca.indeed.com/viewjob?jk=ae2a14acdc7258ba",
        None,None),("Hatchways","yes","https://ca.indeed.com/viewjob?jk=c71fd8608152d5d3","Jr. Software Developer","none","none")]
        # data = ("o","o","o","o","o","o","o")
        tracker = JobTracker.JobTracker()
        tracker.addjob(data)
        print("added job.")
        tracker.to_file()
        print("converted to JSON.")
        print("done!")
    else:
        try:
            if(os.path.isfile(file[1])):
                print("Do stuff..")
            else:
                print("Not a proper file.")
        except (ValueError,TypeError):
            print("Sorry!")
        except:
            print("Unexpected error.")

    return 0


if __name__ == "__main__":
    import JobTracker
    import sys,os
    main()