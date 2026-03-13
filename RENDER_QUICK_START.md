# Render Deployment - Quick Start

## ✅ Pre-Deployment Status

Your project is **READY TO DEPLOY**! Here's what's already configured:

- ✅ Code pushed to GitHub
- ✅ Database connected and migrated (17 tables created)
- ✅ Static files configured with WhiteNoise
- ✅ Environment variables documented
- ✅ Build script created (`build.sh`)
- ✅ Production settings configured
- ✅ Security settings enabled

## 🚀 Deploy to Render (5 Minutes)

### Step 1: Create Render Account
1. Go to https://render.com
2. Sign up with GitHub account
3. Authorize Render to access your repositories

### Step 2: Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect repository: `mohitchaudhari790/Resume-analyzer`
3. Configure:
   - **Name:** `ai-resume-portal` (or your choice)
   - **Region:** Oregon (US West) - Same as your database
   - **Branch:** `main`
   - **Root Directory:** `ai_resume_portal`
   - **Runtime:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

### Step 3: Set Environment Variables
Click **"Advanced"** → **"Add Environment Variable"**

```bash
SECRET_KEY=django-insecure-CHANGE-THIS-TO-RANDOM-STRING
DEBUG=False
DATABASE_URL=postgresql://aidb_t5fe_user:yw1WOk7SlwrCJ6yRpjo7ALX3MLpu7cDN@dpg-d6oqp27kijhs73aup0j0-a.oregon-postgres.render.com/aidb_t5fe
ALLOWED_HOSTS=.onrender.com
ADMIN_URL=secure-admin-2024
RENDER=True
```

**Generate SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 4: Deploy
1. Click **"Create Web Service"**
2. Wait 5-10 minutes for build
3. Watch logs for any errors

### Step 5: Access Your App
```
https://your-app-name.onrender.com
```

## 📊 Admin Panel Access

```
https://your-app-name.onrender.com/secure-admin-2024/
```

Create superuser after deployment:
```bash
# In Render Shell (Dashboard → Shell)
python manage.py createsuperuser
```

## 🔧 Post-Deployment

### Create Superuser
1. Go to Render Dashboard
2. Click your web service
3. Click **"Shell"** tab
4. Run:
   ```bash
   cd ai_resume_portal
   python manage.py createsuperuser
   ```

### Add Sample Jobs
```bash
cd ai_resume_portal
python manage.py populate_jobs
```

## 📝 Important URLs

| Purpose | URL |
|---------|-----|
| Homepage | `https://your-app.onrender.com/` |
| Login | `https://your-app.onrender.com/login/` |
| Register | `https://your-app.onrender.com/register/` |
| Dashboard | `https://your-app.onrender.com/dashboard/` |
| Admin Panel | `https://your-app.onrender.com/secure-admin-2024/` |
| Job Listings | `https://your-app.onrender.com/jobs/` |

## 🐛 Troubleshooting

### Build Fails
- Check `build.sh` has execute permissions
- Verify `requirements.txt` is correct
- Check Python version in `runtime.txt`

### Static Files Not Loading
- Verify `STATIC_ROOT` is set
- Check WhiteNoise is in `MIDDLEWARE`
- Run `python manage.py collectstatic` in Shell

### Database Connection Error
- Verify `DATABASE_URL` is correct
- Check database is in same region
- Ensure migrations ran during build

### 500 Internal Server Error
- Set `DEBUG=True` temporarily to see error
- Check logs in Render Dashboard
- Verify all environment variables are set

## 📱 Monitor Your App

### View Logs
Render Dashboard → Your Service → Logs

### Check Health
```bash
curl https://your-app.onrender.com/
```

### Database Status
```bash
# In Render Shell
cd ai_resume_portal
python test_db_connection.py
```

## 🔄 Update Deployment

After making changes:
```bash
git add .
git commit -m "Your changes"
git push origin main
```

Render automatically redeploys!

## 💡 Tips

1. **Free Tier:** Render free tier spins down after 15 minutes of inactivity
2. **First Request:** May take 30-60 seconds to wake up
3. **Custom Domain:** Add in Render Dashboard → Settings → Custom Domain
4. **SSL:** Automatically provided by Render
5. **Logs:** Keep logs tab open during first deployment

## 🎉 Success Indicators

- ✅ Build completes without errors
- ✅ Service shows "Live" status
- ✅ Homepage loads successfully
- ✅ Login/Register works
- ✅ Static files (CSS/JS) load
- ✅ Database queries work
- ✅ Admin panel accessible

## 📞 Support

- **Render Docs:** https://render.com/docs
- **Django Docs:** https://docs.djangoproject.com
- **GitHub Issues:** https://github.com/mohitchaudhari790/Resume-analyzer/issues

---

**Your database is already set up and migrated!**
**Just create the web service and deploy!** 🚀
