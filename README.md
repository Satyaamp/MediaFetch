# MediaFetch → Search, View and Download Instantly

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.0-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

A Flask web application that allows users to search, view and download images and videos from Pixabay API. The application features a clean, responsive interface for browsing trending media content and searching through millions of free images and videos.

## Features

- **Trending Content**: View popular images and videos on the homepage
- **Advanced Search**: Search media by keywords with category filtering
- **Media Categories**: Filter by fashion, electronics, sports, food, travel, nature
- **Download Functionality**: Download images and videos with unique filenames
- **Autocomplete**: Smart search suggestions as you type
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Pagination**: Navigate through search results efficiently

## Installation

### Prerequisites

- Python 3.7+
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mediafetch
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   - Create a `.env` file in the root directory
   - Add your Pixabay API key:
     ```
     PIXABAY_API_KEY=your_api_key_here
     FLASK_ENV=development
     FLASK_DEBUG=true
     ```

4. **Get Pixabay API Key**
   - Visit [Pixabay API](https://pixabay.com/api/docs/)
   - Sign up for a free account
   - Get your API key from the dashboard

## Usage

### Running the Application

1. **Development Mode**
   ```bash
   python app.py
   ```
   The application will start on `http://127.0.0.1:5000`

2. **Production Mode**
   ```bash
   # Set environment variables
   export FLASK_ENV=production
   export FLASK_DEBUG=false

   # Run with production server
   gunicorn app:app
   ```

### Using the Application

1. **Homepage**: Browse trending images and videos
2. **Search**: Use the search bar to find specific content
3. **Filter**: Select categories to narrow down results
4. **Download**: Click download buttons to save media files
5. **Autocomplete**: Start typing to get search suggestions

## Project Structure

```
mediafetch/
├── app.py                
├── requirements.txt       
├── .env                   
├── .gitignore            
├── README.md             
├── static/              
│   ├── css/
│   │   └── style.css
│   ├── downloads/        
│   └── images/           
└── templates/           
    ├── index.html        
    └── results.html    
```

## API Configuration

The application uses the Pixabay API to fetch media content. The API key should be stored in the `.env` file for security.

### API Endpoints Used

- **Images**: `https://pixabay.com/api/?key={API_KEY}&q={query}&category={category}`
- **Videos**: `https://pixabay.com/api/videos/?key={API_KEY}&q={query}&category={category}`
- **Trending**: `https://pixabay.com/api/?key={API_KEY}&editors_choice=true`

### Rate Limits

- Free tier: 100 requests per hour
- Upgrade available for higher limits

## Dependencies

- **Flask**: Web framework
- **requests**: HTTP library for API calls
- **python-dotenv**: Environment variable management

## Security

- API keys are stored in environment variables
- `.env` file is excluded from version control
- User-Agent headers are set for API requests
- Input validation and error handling included

## Development

### Adding New Features

1. Create new routes in `app.py`
2. Add corresponding templates in `templates/`
3. Update static files in `static/` as needed
4. Test thoroughly before deployment

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Comment complex logic

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `.env` file exists and contains valid API key
   - Check that `python-dotenv` is installed

2. **Port Already in Use**
   ```bash
   # Kill process using port 5000
   lsof -ti:5000 | xargs kill -9
   ```

3. **Missing Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Debug Mode

Enable debug mode by setting in `.env`:
```
FLASK_DEBUG=true
FLASK_ENV=development
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
- Check the troubleshooting section
- Review the Pixabay API documentation
- Create an issue in the repository

## Developed By
<table align="center" style="background-color:#f0f0f0; padding:15px; border-radius:10px;">
 <tr>
    <td align="center">
      <img src="https://github.com/Satyaamp.png" width="100"><br>
      <strong>Satyam Kumar</strong><br>
      <a href="https://github.com/Satyaamp" title="GitHub">
        <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" width="30" alt="GitHub"/>
      </a>
      <a href="https://x.com/whosatyamkr" title="X">
        <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/x.svg" width="30" style="color:#1DA1F2" alt="X"/>
      </a>
      <a href="https://www.linkedin.com/in/satyaamp/" title="LinkedIn">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="30" alt="LinkedIn"/>
      </a>
    </td>
</tr>
</table>





---

