<img width="1600" height="900" alt="Gitub" src="https://github.com/user-attachments/assets/f78f7c3d-1ae8-4832-8f78-f09bb50f657d" />

<img width="1600" height="900" alt="hotel_haven_github_banner_light" src="https://github.com/user-attachments/assets/ca83da7c-f5b3-4c36-8d71-d7b5e10d2be4" />

# Can We Predict Hotel Booking Cancellations Before They Happen?
Analyzing booking behavior to help hotels reduce revenue loss. So I worked on a predictive analytics project to understand the booking behavior behind cancellations and build a model that can help identify high-risk bookings before they happen

Can we predict hotel booking cancellations before they happen?

That was the question behind my latest data science project: Hotel Haven Booking Cancellation Prediction Model.

Hotel Haven, a luxury hotel chain, was facing a familiar hospitality problem: customers make reservations, but a significant number later cancel. For a hotel, that does not just mean an empty room. It means lost revenue, poor resource planning, unstable demand forecasting, and missed opportunities to retain customers earlier.

## Problem Statement
hotel struggles with high cancellation rates, leading to lost revenue and inefficient resource allocation. The existing system does not provide sufficient insights into why customers cancel their bookings. The hotel management seeks to predict cancellations based on booking data to improve operational efficiency and customer retention.

So I worked on a predictive analytics project to understand the booking behavior behind cancellations and build a model that can help identify high-risk bookings before they happen.

## Findings
<img width="2096" height="1407" alt="C 2" src="https://github.com/user-attachments/assets/1cec7d43-b8cd-41b7-8645-a5393c00199a" />

<img width="2164" height="1407" alt="C 4" src="https://github.com/user-attachments/assets/3ed91b7c-7154-4eb5-af73-dbc31f8ee52c" />

The analysis shows that **67.23% of Hotel Haven bookings were not cancelled**, representing **24,396 bookings**, while **32.77% were cancelled**, representing **11,889 bookings**. This means that almost **one in every three bookings** ended in cancellation, making cancellation prediction a serious business concern for the hotel.
 <img width="1768" height="1362" alt="C 1" src="https://github.com/user-attachments/assets/1748c9eb-4adb-4e02-819f-aa2d741ca568" />

<img width="3432" height="1466" alt="C 5" src="https://github.com/user-attachments/assets/5298cbfc-f2e2-45a3-acff-cd67c60d36d3" />

A closer look at booking price patterns shows that customers within the **$101–$200 average price range** recorded the highest cancellation behavior, followed by customers in the **$0–$100 price range**. On the other hand, premium customers within the **$301–$540 price range** recorded very low cancellation levels. This suggests that lower and mid-priced bookings are more exposed to cancellation risk, while premium customers appear to show stronger booking commitment.
<img width="1768" height="1361" alt="C 6" src="https://github.com/user-attachments/assets/762208e8-984d-4df6-81b6-69d46292ddeb" />

Revenue analysis also reveals an encouraging insight: a larger share of Hotel Haven’s revenue came from customers who did not cancel their bookings. About **62% of total revenue** was generated from retained bookings, showing the strong revenue value of customers who follow through with their reservations.
<img width="3570" height="1466" alt="C 12" src="https://github.com/user-attachments/assets/f8dcc64e-5258-49c6-9d16-69d841fbf6f1" />

<img width="3570" height="1466" alt="C 12" src="https://github.com/user-attachments/assets/e919ee32-3323-46cd-aa21-caedf14db7ff" />

To better understand customer cancellation behavior, lead time and average price were grouped into categories. The analysis clearly shows that **lead time is one of the strongest drivers of cancellation**. Customers who booked far ahead of their check-in date were more likely to cancel compared to those with shorter reservation windows.

<img width="1618" height="1361" alt="C 9" src="https://github.com/user-attachments/assets/5e149bdc-6611-44a8-aa95-7078fd7a23d8" />

<img width="1618" height="1361" alt="C 8" src="https://github.com/user-attachments/assets/143fa3ac-b587-46e4-8be6-42d50c498dbf" />

Even after testing different lead-time categories, the pattern remained consistent. As the time between booking and check-in increased, cancellation risk also increased across most price categories. This indicates that long lead-time bookings require closer monitoring and proactive customer engagement.

Market segment analysis shows that **online bookings had the highest cancellation rate at 30%**, making them one of Hotel Haven’s biggest cancellation-risk channels. This may be linked to the ease of making and cancelling online reservations, which can contribute to revenue loss and inefficient room planning.

In contrast, **corporate customers recorded only an 11% cancellation rate**, showing stronger booking commitment. This makes the corporate segment a more stable and predictable source of revenue for Hotel Haven.
<img width="2970" height="1466" alt="C 11" src="https://github.com/user-attachments/assets/b8346e7a-61d0-4468-b90f-1a73a35e1b10" />

Complementary bookings recorded a **0% cancellation rate**. Although these bookings may not generate direct revenue, they can still support the hotel through referrals, brand visibility, guest relationships, and positive reviews.

Customer type also played an important role. **One-time customers accounted for a larger portion of average revenue but were also more likely to cancel**, with a cancellation rate above **34%**. Repeat customers, however, showed much stronger commitment and a lower cancellation rate, making them valuable for long-term customer retention.
<img width="1688" height="1361" alt="C 13" src="https://github.com/user-attachments/assets/cbefaffc-bef1-44df-b4f7-4f02e87770fc" />

The analysis further shows that customers who made more special requests were less likely to cancel their bookings. Guests with fewer or no special requests had higher cancellation rates, suggesting that special requests may indicate stronger interest, clearer travel plans, or deeper commitment to the booking.
<img width="1688" height="1361" alt="C 14" src="https://github.com/user-attachments/assets/14ba669f-6558-48b3-96b9-ff98bf986038" />

Room type analysis shows that **Room Type 6 had the highest cancellation risk at 42%**, followed by **Room Type 4 at 34%**. Meanwhile, **Room Type 7 recorded the lowest cancellation risk at 23%**. However, room type alone does not appear to be a strong standalone predictor of cancellation, as the differences may also depend on other factors such as price, customer type, booking channel, and lead time.
<img width="2990" height="1869" alt="C 15" src="https://github.com/user-attachments/assets/7ef117d4-007b-4a5e-91e6-f25597ee5f25" />

Overall, the key insight from the analysis is clear: **Hotel Haven’s cancellation risk is strongly influenced by lead time, market segment, customer type, price range, and booking commitment signals such as special requests**. These findings can help the hotel identify high-risk bookings early and design better retention strategies.

## Model Explanation

## Key Features
The key variables captured in this were 16 features, including the Lead time, average price, special requests, room type, market segment type, number of nights, date of reservation and the target variable (booking status).

## Tools and Libraries

Python (Jupyter Notebook)

Pandas

Matplotlib

Seaborn

Scikit-Learn

XGBoost

Imbalanced-Learn

## Data Preprocessing
Following business and data understanding, the data was cleaned during which invalidate date was corrected, data types were fixed and dropped irrelevant dropped. Column engineering was implored to generating the total nights, total revenue, price range, and lead time range. Categorical variables were encoded. RobustScaler was applied to handle skewed numerical features. Class Imbalance (67:33 class distribution) was identified and handled using SMOTE. A final cross validation was done before training.

## Exploratory Data Analysis
A comprehensive analysis, both univariate and bivariate was done to uncover cancellation patterns.

## Machine Learning Model
The hotel cancellation predictive model was built using a supervised machine learning approach. The class sets were split into 80:20 for training and testing. Multiple classification algorithms were experimented with, including but not limited to

Logistic Regression

Random Forest Classifier

Gradient Boosting

XGBoost

AdaBoost

Support Vector Machine

K-Nearest Neighbors

Decision Tree The best performing model was selected and underwent hyperparameter tuning to improve its performance

## Evaluation Metrics
The following metrics were used to assess the performance of the model:

Accuracy: The overall proportion of correctly predicted booking status (both cancelled and not-cancelled)
Precision: The proportion of correctly identified cancelled bookings among all bookings classified as cancelled (false alarm rate)
Recall: The proportion of correctly identified cancellations among all actual cancelled bookings (correctly flagged cancellation)
F1-score: The harmonic mean of precision and recall, providing a balanced metric for model evaluation
ROC-AUC score: The ability of the model to distinguish between class

## Recommendations

1. **Strengthen booking commitment**
   Introduce deposits, prepaid rates, or credit card guarantees to reduce casual bookings and encourage customers to commit before arrival.

2. **Create flexible alternatives to full cancellation**
   For lower-priced rooms, offer options such as rescheduling, partial refunds, or booking credits instead of full cancellation. This gives budget-conscious guests a reason to retain their booking.

3. **Reward direct and offline bookings**
   Encourage guests who book directly or through offline channels by offering room upgrades, loyalty points, discounts on future stays, or exclusive guest benefits.

4. **Proactively manage long lead-time bookings**
   Identify bookings made far in advance and engage those guests early through personalized messages, promotional upgrades, reminder campaigns, and curated experience packages.

5. **Offer retention incentives for long-lead bookings**
   Provide small incentives such as complimentary breakfast, late checkout, room upgrades, or discount vouchers to guests who keep long-lead reservations.

6. **Improve room listing accuracy**
   Ensure that room descriptions, photos, amenities, and prices accurately reflect the real guest experience. Clear and honest listings can reduce dissatisfaction-driven cancellations.

7. **Grow the corporate customer segment**
   Actively pursue corporate clients through contract negotiations, corporate rate agreements, and partnerships with companies and travel agencies. Corporate guests showed stronger booking commitment and can provide a more stable revenue stream.

8. **Expand special-request options**
   Add more detailed special-request fields during booking to increase customer engagement and better capture guest preferences. Customers who make special requests may have stronger booking intention, making this a useful signal for retention planning.

