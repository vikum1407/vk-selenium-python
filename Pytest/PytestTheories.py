'''

    Pytest Rules:

        * Should file start with 'test or end with 'test
        * All test can execute by 'py.test' command. it will execute all test file in the folder
        * If you need to run the specific test, go inside the folder and 'py.test <file-name>'
        If you need to run specific method by keyword,
            - py.test -k <method name-this can be just part of word in method> -v( mean more information's )
            eg:-
                def test_login():
                    assert 'admin' == 'admin'

                py.test -k login -v

    Execution Report:

        F..FFF => F mean test fail
               => '.' (green dot) mean test pass


    How to group the pytests:-

        * you can use,
            '@pytest.mark.<groupName>' then run with 'pytest -m <groupName> [here run all the file selected group tag]

        * If you need to run specific file
            '@pytest.mark.<groupName> <fileName> -m <groupName>

    How to execute parallel:-

        * Have to install a package
            pip install pytest-xdist

        * Execution command
            py.test -n 5 <5 mean 5 browsers in parallel> [here run all tests>

            If you need to run specific test file,
            py.test <file name> -n 4


    Pytest Fixtures:-

        * Have to use 'setup_module' and 'teardown_module' method for that (if you are using fixtures, no need to have those two methods)
        * Have to mention '@pytest.fixture(scope='module')' in you above methods
        * yield - this mean execute after executing of the all method

        Fixtures in Class level:-

            * initiate class and see the test_fixtureInClass.py file


    Pytest HTML Reports:-

        * Have to install 'pip install pytest-html'
        * Run command
            - pytest <file name> -v -s --html=google_test_report.html


        -v using for -
            need to get more details when executing

        -s using for -
            need to print() things on the log


    Pytest in Conftest

        * Create 'conftest.py' give the name same as this

    Pytest Global pytest

    Pytest parameterize




'''