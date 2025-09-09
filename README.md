# TaskManagement Görev Yönetimi API  

Bu proje, **Supabase** altyapısı ve **FastAPI** framework’ü kullanılarak geliştirilmiş bir Görev Yönetimi API uygulamasıdır.  
Amaç, kullanıcıların kendi görevlerini oluşturabilmesi, listeleyebilmesi, güncelleyebilmesi ve silebilmesini sağlayan **güvenli ve modern bir backend çözümü** sunmaktır. 🚀  

---

## ⚙️ Teknolojiler ve Bileşenler  
- **Python 3.9+**  
- **FastAPI** → Modern, tip güvenli web framework  
- **Supabase** → Postgres veritabanı, Auth, Storage, Realtime özellikleri  
- **Supabase-Py** → Python için resmi Supabase istemcisi  
- **Uvicorn** → ASGI server  

---

## 📝 İş Listesi (Task Breakdown)  

### 1. Supabase Yapılandırması  
- Supabase projesi oluştur  
- `tasks` tablosu oluştur  
- RLS (Row Level Security) kuralları ekle  
- JWT doğrulaması için Auth ayarlarını yap  

### 2. Backend Kurulumu  
- `supabase-py` ve `fastapi` bağımlılıklarını yükle  
- `.env` üzerinden Supabase bağlantısını ayarla  
- FastAPI başlat (`Uvicorn` ile)  

### 3. CRUD Endpoint’leri  
- `POST /tasks/` → Yeni görev oluşturma  
- `GET /tasks/` → Kullanıcıya özel görevleri listeleme  
- `PUT /tasks/{id}` → Görev güncelleme (örn. tamamlandı)  
- `DELETE /tasks/{id}` → Görev silme  

### 4. Kimlik Doğrulama & Güvenlik  
- JWT token doğrulama mekanizması ekle  
- Kullanıcı `user_id` bilgisini Supabase Auth’tan al  
- Yanlış erişimlerde `403 Forbidden` döndür  

### 5. Ekstra Özellikler (Opsiyonel)  
- Görev kategorileri (örn. `work`, `personal`)  
- Deadline tarihi (`due_date` alanı)  
- Realtime desteği → görevlerin anlık güncellenmesi  
- Görev ekine dosya yükleme (Supabase Storage)  

---

## 🎯 Hedef  
Bu proje ile:  
- Supabase veritabanı ve Auth modülünü Python’dan nasıl kullanacağını öğreneceksin,  
- FastAPI ile REST API geliştirme pratiği kazanacaksın,  
- CRUD ve güvenlik mekanizmalarıyla modern bir Görev Yönetimi API geliştirmiş olacaksın.  
