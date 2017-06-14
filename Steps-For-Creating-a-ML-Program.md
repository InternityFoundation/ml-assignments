					STEPS FOR CREATING A MACHINE LEARNING PROGRAM
			
(i) Importing Required Packages: We would need to import packages as and when required in our program as per the requirements. These packages are similar to header files in programming languages such as C/C++. They contain a bunch of functions developed by various developers to perform certain tasks and can be used easily. We need not write their logic from scratch and they are very well optimised to save our time and memory space both. If you face any type of import errors then make sure that the package which you are trying to use is already installed.

(ii) Loading Data: We would have to find a particular dataset on which we are interested to prepare a ML model and then load them into our program or we can use some of the famous or very popularly used datasets (like Iris dataset) which can be used by directly importing some packages. For importing data  from CSV (Comma Seperated Values) file or text files we can use either NumPy or Pandas. I recommend using pandas dataframes as they provide lot of flexibilities such as inluding headers or not and various other which you can explore.

(iii) Data Cleaning: We need to perform data cleaning if required. It involves removing tupples or records which are redundant or repeated or if have missing values. Another way to deal with missing values is to fill them by using various measures of central tendencies such as mean/median depending on the situation. Generally if a record has multiple fields missing we prefer to remove that record and if it has less number of fields or features missing we can use mean/median to fill those missing values.

(iv) Finding Appropriate Algorithm: After performing data cleaning we need to explore an appropriate algorithm for solcing our problem. We can explore sklearn/scikit-learn package in python for ML functions. It would contain almost any required ML algorithm. It is basic scientific kit/library of ML.

After we have identified our required function we also need to see its usage and various parameters which are supplied to that function to improve its accuracy.

(v) Data Representation: Also note if you need to pictorially represent your datasets you can always use matplotlib library. It can be very useful to represent our data using graphs or plots. We are not using it here but remember it should be used to present or explain your point to some else.

Sometimes feature engineering is also performed after this if we have many variables or parameters in our dataset and we need to keep only essential features in order to improve its accuracy.

(vii) After this comes the most essential step. Splitting our dataset into two partitions. One for training purpose and another for testing purpose.

This can be done using inbuilt train_test_split function available to us. If we are working in some other programming language and you do not have this train_test_split function then we divide the dataset ourselves into 60:40 ratio where 60% is used for training and 40% is used for testing (A rule that is followed generally).

(viii) Then feed our chosen algorithm, in this case Logistic Regression function with train data to learn patterns and identity which type of data points belong to which classes.

This can also be done easily by using fit function which basically fits the train dataset into the algorithm.

(ix) After we are done with this, we have basically trained our model. Remember the larger the train dataset the better it would be able to distinguish between various classes. Also tuning of parameters used in our function also plays a vital role.

(x) Now we are ready to test our model. We can use our trained model to predict the outcome of test datasets.

And to check how well it performed we can compare our results with actual classes of these test datasets.

(xi) Lastly, you can find accuracy of the model using various functions of "metrics" sub package available in python.

You don't need to panic. I also don't remember all these functions and their usage. But you can always Google about them. A very good documentation of these  functions is available online.
