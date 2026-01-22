def get_custom_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: #f5f8fc;
    }
    
    /* Fix text visibility */
    .stMarkdown, .stText, p, span, div, h1, h2, h3, h4, h5, h6, label {
        color: #2c3e50 !important;
    }
    
    /* Input fields */
    .stTextInput input, .stSelectbox select, .stDateInput input, .stNumberInput input {
        color: #2c3e50 !important;
        background: #ffffff !important;
        border: 1.5px solid #e8eef5 !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
        transition: all 0.2s ease !important;
    }
    
    .stTextInput input:focus, .stSelectbox select:focus, .stDateInput input:focus {
        border-color: #7fa8e8 !important;
        box-shadow: 0 0 0 3px rgba(127, 168, 232, 0.1) !important;
    }
    
    .main-header {
        background: linear-gradient(135deg, #5b7dd6 0%, #7fa8e8 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin-bottom: 2.5rem;
        box-shadow: 0 8px 20px rgba(91, 125, 214, 0.2);
    }
    
    .main-header h1, .main-header p {
        color: white !important;
    }
    
    .main-header h1 {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    
    .card {
        background: #ffffff;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        margin-bottom: 2rem;
        border: 1px solid #e8eef5;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f9fbfd 0%, #ffffff 100%);
        padding: 2rem;
        border-radius: 14px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        border-left: 5px solid #7fa8e8;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(91, 125, 214, 0.15);
        background: #ffffff;
        border-left-color: #5b7dd6;
    }
    
    .metric-card h3 {
        color: #7c8fa3 !important;
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        margin: 0 0 0.5rem 0 !important;
    }
    
    .metric-card h2 {
        color: #2c3e50 !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        margin: 0.5rem 0 !important;
    }
    
    .success-banner {
        background: linear-gradient(135deg, #5cb85c 0%, #6fc976 100%);
        color: white !important;
        padding: 1.4rem 1.6rem;
        border-radius: 10px;
        font-weight: 600;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(92, 184, 92, 0.2);
    }
    
    .success-banner * {
        color: white !important;
    }
    
    .alert-box {
        background: linear-gradient(135deg, #fef8e8 0%, #fffbf0 100%);
        border-left: 5px solid #f0c87c;
        padding: 1.2rem 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(240, 200, 124, 0.1);
    }
    
    .alert-box strong, .alert-box * {
        color: #8b7a3f !important;
    }
    
    .error-box {
        background: linear-gradient(135deg, #fdeaea 0%, #ffe8e8 100%);
        border-left: 5px solid #f08080;
        padding: 1.2rem 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(240, 128, 128, 0.1);
    }
    
    .error-box strong, .error-box * {
        color: #a84a4a !important;
    }
    
    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #7fa8e8 0%, #5b7dd6 100%);
        color: white !important;
        border: none;
        padding: 0.85rem 1.8rem;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 0.3px;
        box-shadow: 0 4px 12px rgba(91, 125, 214, 0.2);
    }
    
    div[data-testid="stButton"] button:hover {
        background: linear-gradient(135deg, #5b7dd6 0%, #4a5fb8 100%);
        box-shadow: 0 8px 20px rgba(91, 125, 214, 0.35);
        transform: translateY(-2px);
    }
    
    div[data-testid="stButton"] button:active {
        transform: translateY(0);
    }
    
    .section-title {
        color: #2c3e50 !important;
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        margin-bottom: 1.5rem !important;
        padding-bottom: 0.75rem !important;
        border-bottom: 3px solid #e8eef5 !important;
    }
    
    .login-container {
        background: #ffffff;
        border-radius: 18px;
        padding: 3.5rem;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
        max-width: 450px;
        margin: 0 auto;
        border: 1px solid rgba(127, 168, 232, 0.1);
    }
    
    .login-container h1, .login-container p, .login-container label {
        color: #2c3e50 !important;
    }
    
    .logout-btn button {
        background: linear-gradient(135deg, #e89999 0%, #d87a7a 100%) !important;
        border-color: #d87a7a !important;
        box-shadow: 0 4px 12px rgba(232, 153, 153, 0.2) !important;
    }
    
    .logout-btn button:hover {
        box-shadow: 0 8px 20px rgba(232, 153, 153, 0.35) !important;
    }
    
    .exam-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        border: 1px solid #e8eef5;
        transition: all 0.3s ease;
    }
    
    .exam-card:hover {
        border-color: #7fa8e8;
        box-shadow: 0 8px 20px rgba(91, 125, 214, 0.12);
        transform: translateY(-2px);
    }
    
    .exam-card h3, .exam-card p, .exam-card strong, .exam-card div {
        color: #2c3e50 !important;
    }
    
    .badge {
        display: inline-block;
        padding: 0.4rem 0.9rem;
        border-radius: 14px;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.3px;
    }
    
    .badge-blue {
        background: linear-gradient(135deg, #e8f2ff 0%, #dbeafe 100%);
        color: #5b7dd6 !important;
        box-shadow: 0 2px 6px rgba(91, 125, 214, 0.1);
    }
    
    .badge-green {
        background: linear-gradient(135deg, #e8f5e9 0%, #d4edda 100%);
        color: #4a7a5c !important;
        box-shadow: 0 2px 6px rgba(74, 122, 92, 0.1);
    }
    
    .badge-orange {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        color: #a87a3f !important;
        box-shadow: 0 2px 6px rgba(168, 122, 63, 0.1);
    }
    
    /* Fix Streamlit native components */
    .stAlert {
        color: #2c3e50 !important;
        border-radius: 10px !important;
    }
    
    .stDataFrame {
        color: #2c3e50 !important;
        border-radius: 10px !important;
    }
    
    /* Fix expander */
    .streamlit-expanderHeader {
        color: #2c3e50 !important;
        background: #f9fbfd !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    
    /* Fix checkbox and radio */
    .stCheckbox label, .stRadio label {
        color: #2c3e50 !important;
        font-weight: 500 !important;
    }
    
    /* Sidebar styling - MENU CLAIR */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8fafb 0%, #f3f6fa 100%) !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] {
        background: transparent;
    }
    
    [data-testid="stSidebar"] .stTabs [role="tablist"] button {
        background: transparent !important;
        border-color: #e8eef5 !important;
        color: #2c3e50 !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stSidebar"] .stTabs [role="tablist"] button[aria-selected="true"] {
        background: linear-gradient(90deg, #7fa8e8 0%, #5b7dd6 100%) !important;
        color: white !important;
        border-color: #5b7dd6 !important;
        box-shadow: 0 4px 12px rgba(91, 125, 214, 0.25) !important;
    }
    
    [data-testid="stSidebar"] .stTabs [role="tablist"] button:hover {
        background: rgba(123, 168, 232, 0.1) !important;
        color: #5b7dd6 !important;
    }
    
    [data-testid="stSidebar"] a {
        color: #2c3e50 !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }
    
    [data-testid="stSidebar"] a:hover {
        color: #7fa8e8 !important;
        background: rgba(127, 168, 232, 0.12) !important;
        border-radius: 8px !important;
    }
    
    [data-testid="stSidebar"] .stRadio {
        background: transparent;
    }
    
    [data-testid="stSidebar"] [role="option"] {
        background: transparent !important;
        color: #2c3e50 !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }
    
    [data-testid="stSidebar"] [role="option"][aria-selected="true"] {
        background: linear-gradient(90deg, rgba(127, 168, 232, 0.2) 0%, rgba(91, 125, 214, 0.15) 100%) !important;
        color: #5b7dd6 !important;
        font-weight: 700 !important;
        box-shadow: inset 0 2px 8px rgba(91, 125, 214, 0.1) !important;
    }
    
    [data-testid="stSidebar"] [role="option"]:hover {
        background: rgba(123, 168, 232, 0.12) !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox {
        background: #ffffff !important;
        border-radius: 8px !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox div {
        background: #ffffff !important;
        border-radius: 8px !important;
    }
    
    /* Page navigation pages links */
    [data-testid="stSidebarNav"] li a {
        border-radius: 10px;
        margin: 0.6rem 0;
        padding: 0.9rem 1.2rem;
        color: #2c3e50 !important;
        transition: all 0.2s ease;
        font-weight: 600;
    }
    
    [data-testid="stSidebarNav"] li a:hover {
        background: rgba(127, 168, 232, 0.15) !important;
        color: #5b7dd6 !important;
        transform: translateX(4px);
    }
    
    [data-testid="stSidebarNav"] li a[aria-current="page"] {
        background: linear-gradient(90deg, rgba(127, 168, 232, 0.25) 0%, rgba(91, 125, 214, 0.2) 100%) !important;
        color: #5b7dd6 !important;
        border-left: 5px solid #5b7dd6 !important;
        font-weight: 700 !important;
        box-shadow: 0 2px 8px rgba(91, 125, 214, 0.15) !important;
    }
    
    /* Sidebar header */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #2c3e50 !important;
        font-weight: 700 !important;
    }
    
    /* Sidebar text */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #2c3e50 !important;
    }
    
    /* Divider in sidebar */
    [data-testid="stSidebar"] hr {
        border-color: #e8eef5 !important;
    }
    
    /* Tabs styling */
    [role="tablist"] {
        border-bottom: 2px solid #e8eef5 !important;
    }
    
    [role="tab"] {
        color: #7c8fa3 !important;
        font-weight: 600 !important;
    }
    
    [role="tab"][aria-selected="true"] {
        color: #5b7dd6 !important;
        border-bottom: 3px solid #5b7dd6 !important;
    }
    
    /* Tables */
    .stDataFrame {
        border-radius: 12px !important;
    }
    
    .stDataFrame tbody tr:hover {
        background-color: rgba(127, 168, 232, 0.05) !important;
    }
    
    /* General improvements */
    hr {
        border-color: #e8eef5 !important;
    }
    </style>
    """