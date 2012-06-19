import nose
import sys,os, os.path


def runmodels():
    testdir = os.path.normpath('./tests/models/')
    configfile = os.path.join(os.path.normpath('./config/'), "nose.cfg")
    argv = [ configfile,testdir]
    nose.run(argv=argv)
    return

def runcontrollers():
    testdir = os.path.normpath('./tests/controllers/')
    configfile = os.path.join(os.path.normpath('./config/'), "nose.cfg")
    argv = [ configfile,testdir]
    nose.run(argv=argv)
    return

def runall():
    runmodels()
    runcontrollers()
    testdir = os.path.normpath('./tests/others/')
    configfile = os.path.join(os.path.normpath('./config/'), "nose.cfg")
    argv = [ configfile,testdir]
    nose.run(argv=argv)
    return
    
if __name__ == "__main__":
    #print len(sys.argv), "  ", sys.argv
    if len(sys.argv) == 1 or sys.argv[1] == "all":
        print "running all tests"
        runall()
    elif sys.argv[1] == "models":
        print "running model tests"
        runmodels()
    elif sys.argv[1] == "controllers":
        print "running controller tests"
        runcontrollers()
    else:
        print "Usage: runtests < all OR models OR controllers >"
        sys.exit(0)
    sys.exit(0)
        
    