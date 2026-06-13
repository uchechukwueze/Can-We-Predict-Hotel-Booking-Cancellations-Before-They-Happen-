
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
