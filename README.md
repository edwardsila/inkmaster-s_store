# 🎨 Tattoo E-Commerce Store

Welcome to the **Tattoo E-Commerce Store**, your one-stop shop for all things tattoo-related! Whether you’re a professional tattoo artist or a tattoo enthusiast, we offer high-quality products that cater to all your needs.

## 🌟 Features
- **🛍️ Easy Shopping**: Browse through our wide range of tattoo products.
- **🖌️ Categories**: Organized categories for easy navigation.
- **🛒 Seamless Checkout**: Secure payment processing and order tracking.
- **👤 User Authentication**: Sign up and manage your account.

### 1. **User Authentication**
   - Secure user registration and login system.
   - User profiles with order history and saved preferences.

### 2. **Product Browsing & Search**
   - Browse through a wide range of tattoo-related products.
   - Categories include:
     - **Aftercare products**
     - **Tattoo kits**
     - **Power supplies**
     - **Inks**
     - **Tattoo Needles and Cartridges**
     - **Tattoo Machines**
     - 
### 3. **Shopping Cart & Checkout**
   - Easily add products to your cart.
   - Simple and secure checkout process with multiple payment options.
   - Track your orders either shipped or not shipped through the app.
   - 

### 4. **Admin Dashboard**
   - Manage products, orders, and users from the backend.
   - View sales reports, product inventory, and user activity.

### 6. **Responsive Design**
   - Fully optimized for desktop, tablet, and mobile devices.
   - Enjoy a seamless experience across all screen sizes.

---

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript (ES6), Bootstrap
- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Authentication**: Django AllAuth
- **Payment Gateway**: PayPal, Stripe
- **Deployment**: Railway.app
- **Domain**: [InkMasters](https://ke254.tech)

---

## Screenshots

![Homepage Screenshot](static/assets/img/homepage-screenshot.png)
> A look at our user-friendly homepage featuring the latest products and offers.

---

## Demo Video

Watch the demo video for a complete overview of InkMasters on [YouTube](https://youtu.be/9JuKRAv6soE).

---

## How to Run InkMasters Locally

1. **Clone the Repository**:
   ```bash
	https://github.com/edwardsila/inkmaster-s_store.git

2. **Activate virtual enviroment**:
   ```bash
        source env/bin/activate

3. **Install dependencies**:
	```bash

	pip install -r requirements.txt

4. **Set up the PostgreSQL database and configure your .env file**:
	```bash

	DATABASE_URL=postgres://username:password@localhost:5432/inkmasters

5. **Apply migrations**:
	```bash

	python manage.py migrate

6. **Run the development server**:
	```bash

	python manage.py runserver

7. **Access the app at**
   ```bash
    http://localhost:8000.
