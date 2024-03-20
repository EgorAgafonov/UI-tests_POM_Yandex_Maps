allure_result:
		allure serve allure_results
allure_report:
		allure generate -c ./allure_results -o ./allure_report
allure_all_tests:
		pytest -v map_page_positive.py --alluredir allure_results
allure_marks_tests:
		pytest -v map_page_positive.py -v -m"" --alluredir allure_results

pytest_all_tests:
		pytest -v map_page_positive.py
pytest_all_tests:
		pytest -v map_page_positive.py

