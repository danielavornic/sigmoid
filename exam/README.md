# EXAM DOCUMENTATION

Dear sigmaritan,

Hope you enjoyed the learning and exploration of the Machine Learning field and you found this field as attractive as we all do. But now it’s time to put all the knowledge accumulated by you into practice. This examination was created with the aim to test your knowledge and to find the level of understanding of the Machine Learning and Data Analysis principles.

The exam will consist of two parts:

1. The exploration of the data set and training of a Machine Learning model on it.
2. The presentation of the insights and results obtained from the work you have done on this data set in a PowerPoint presentation in front of the jury.

The first part should be submitted by loading all the notebooks into a GitHub repository and sending the link to that repository to Eduard Balamatiuc by the 23rd of July 2023, 23:59.

The second part will be presented individually by each sigmaritans that is examined by the jury consisting of the members of the castor and pollux teams. The date of the presentation will be agreed upon personally with each person and the jury.

## TASK #1

In the archive, you have a CSV file. This file is the data that you should use during the exam passing.

In your case

A company which is active in Big Data and Data Science wants to hire data scientists among people who successfully pass some courses which conduct by the company. Many people signup for their training. Company wants to know which of these candidates are really wants to work for the company after training or looking for a new employment because **it helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates**. Information related to demographics, education, experience are in hands from candidates signup and enrollment.

This dataset designed to understand the factors that lead a person to leave current job for HR researches too. By model(s) that uses the current credentials,demographics,experience data you will **predict the probability of a candidate to look for a new job or will work for the company, as well as interpreting affected factors on employee decision.**

The whole data divided to train and test. Target isn't included in test but the test target values data file is in hands for related tasks.

Note:

- The dataset is imbalanced.
- Most features are categorical (Nominal, Ordinal, Binary), some with high cardinality.
- Missing imputation can be a part of your pipeline as well.

### Features

- enrollee_id: Unique ID for candidate
- city: City code
- city_development_index : Developement index of the city (scaled)
- gender: Gender of candidate
- relevent_experience: Relevant experience of candidate
- enrolled_university: Type of University course enrolled if any
- education_level: Education level of candidate
- major_discipline: Education major discipline of candidate
- experience: Candidate total experience in years
- company_size: No of employees in current employer's company
- company_type: Type of current employer
- last_new_job: Difference in years between previous job and current job
- training_hours: training hours completed
- target: 0 – Not looking for job change, 1 – Looking for a job change

Inspiration (ideas)

- Predict the probability of a candidate will work for the company
- Interpret model(s) such a way that illustrate which features affect candidate decision

In this task, you should:

1. Load and analyze the data set, and try to extract insights from the data.
2. Prepare the data to machine learning algorithm ready format,
3. Handle the NaN values in the data set.
4. Apply some post-processing and post-analysis techniques such as Feature Selection, Feature Engineering, or others and see if they can help you.
5. Create a model or a Pipeline that will show the best performance in predicting the target column.

The target column is **target**. Try to create models that will predict this value.

Some more advice:

- You can split different steps of your work into separated notebooks.
- Commend the code and use the markdown cell type to explain what or why you are doing.
- Explain in a written form the choices and decisions that you made during the processing of the data.
- Use plots, but don’t abuse them.
- Don’t chase a perfect model, better show us why you chose a specific model as the best one.

## TASK #2

Your second task is to create and prepare a presentation on the work that you have done. In the presentation that you should explain the work that you have done and why did you make the choices that you made during the analysis and Machine Learning model development. Some more pieces of advice to the presentation are:

- KISS (Keep It Simple Stupid) - keep the presentation as simple as possible.
- Give some context about the field on which your data set is about.
- Try to avoid as much as possible having a lot of text on your slides.
- Try to tell a story.
- Don’t show the whole process, only the most important findings, and decisions.
- Finish with a conclusion.
- Don’t make lots of slides.

Good luck!
