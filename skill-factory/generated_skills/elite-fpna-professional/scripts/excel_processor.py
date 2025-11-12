"""
Excel Processor Script
Reads and processes financial statements and data from Excel files

Capabilities:
- Read financial statements from Excel workbooks
- Parse multiple sheets (income statement, balance sheet, cash flow)
- Handle various Excel formats and layouts
- Data validation and cleaning
- Extract financial data into structured format
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
import os
from pathlib import Path


class ExcelProcessor:
    """
    Process Excel files containing financial statements and financial data
    """
    
    def __init__(self, file_path: str = None):
        """
        Initialize Excel processor
        
        Args:
            file_path: Path to Excel file
        """
        self.file_path = file_path
        self.workbook_data = {}
        
        if file_path and os.path.exists(file_path):
            self.load_workbook()
    
    def load_workbook(self, file_path: str = None) -> Dict[str, pd.DataFrame]:
        """
        Load all sheets from Excel workbook
        
        Args:
            file_path: Path to Excel file (optional if set in init)
            
        Returns:
            Dictionary with sheet names as keys and DataFrames as values
        """
        if file_path:
            self.file_path = file_path
            
        if not self.file_path:
            raise ValueError("No file path provided")
            
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        
        try:
            # Load all sheets
            excel_file = pd.ExcelFile(self.file_path)
            
            for sheet_name in excel_file.sheet_names:
                self.workbook_data[sheet_name] = pd.read_excel(
                    excel_file, 
                    sheet_name=sheet_name,
                    header=None  # Read without assuming header row
                )
            
            print(f"✓ Loaded {len(self.workbook_data)} sheets from {Path(self.file_path).name}")
            return self.workbook_data
            
        except Exception as e:
            raise Exception(f"Error loading Excel file: {str(e)}")
    
    def find_financial_statement_sheets(self) -> Dict[str, str]:
        """
        Identify which sheets contain income statement, balance sheet, cash flow
        
        Returns:
            Dictionary mapping statement types to sheet names
        """
        statement_sheets = {}
        
        # Common sheet name patterns
        income_patterns = ['income', 'p&l', 'profit', 'loss', 'statement of operations']
        balance_patterns = ['balance', 'position', 'assets']
        cashflow_patterns = ['cash flow', 'cashflow', 'cf', 'statement of cash']
        
        for sheet_name in self.workbook_data.keys():
            sheet_lower = sheet_name.lower()
            
            if any(pattern in sheet_lower for pattern in income_patterns):
                statement_sheets['income_statement'] = sheet_name
            elif any(pattern in sheet_lower for pattern in balance_patterns):
                statement_sheets['balance_sheet'] = sheet_name
            elif any(pattern in sheet_lower for pattern in cashflow_patterns):
                statement_sheets['cash_flow'] = sheet_name
        
        return statement_sheets
    
    def extract_financial_statement(self, sheet_name: str, 
                                   line_item_column: int = 0,
                                   data_columns: List[int] = None) -> pd.DataFrame:
        """
        Extract financial statement data from a sheet
        
        Args:
            sheet_name: Name of sheet to extract
            line_item_column: Column index containing line item names (default: 0)
            data_columns: List of column indices containing financial data
            
        Returns:
            DataFrame with line items as index and periods as columns
        """
        if sheet_name not in self.workbook_data:
            raise ValueError(f"Sheet '{sheet_name}' not found in workbook")
        
        df = self.workbook_data[sheet_name].copy()
        
        # If data columns not specified, use all columns except line item column
        if data_columns is None:
            data_columns = [i for i in range(len(df.columns)) if i != line_item_column]
        
        # Extract line items and data
        line_items = df.iloc[:, line_item_column]
        data = df.iloc[:, data_columns]
        
        # Set line items as index
        data.index = line_items
        
        # Clean column names (use first row if it contains period headers)
        if df.iloc[0, data_columns[0]] is not None:
            try:
                data.columns = df.iloc[0, data_columns].values
                data = data.iloc[1:]  # Remove header row from data
            except:
                data.columns = [f"Period_{i+1}" for i in range(len(data_columns))]
        
        # Remove rows with null line items
        data = data[data.index.notna()]
        
        # Convert to numeric where possible
        for col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='ignore')
        
        return data
    
    def parse_income_statement(self, sheet_name: str = None) -> Dict[str, pd.Series]:
        """
        Parse income statement and extract key line items
        
        Returns:
            Dictionary with standard line items
        """
        if sheet_name is None:
            statements = self.find_financial_statement_sheets()
            sheet_name = statements.get('income_statement')
            
        if sheet_name is None:
            raise ValueError("Income statement sheet not found")
        
        df = self.extract_financial_statement(sheet_name)
        
        # Map common line item names to standard names
        line_item_mapping = {
            'revenue': ['revenue', 'sales', 'total revenue', 'net revenue', 'net sales'],
            'cogs': ['cost of goods sold', 'cogs', 'cost of sales', 'cost of revenue'],
            'gross_profit': ['gross profit', 'gross income'],
            'operating_expenses': ['operating expenses', 'opex', 'total operating expenses'],
            'operating_income': ['operating income', 'operating profit', 'ebit', 'income from operations'],
            'interest_expense': ['interest expense', 'interest', 'interest paid'],
            'ebt': ['earnings before tax', 'ebt', 'income before tax', 'pretax income'],
            'tax_expense': ['tax', 'income tax', 'tax expense', 'provision for taxes'],
            'net_income': ['net income', 'net profit', 'net earnings', 'bottom line']
        }
        
        extracted_items = {}
        
        for standard_name, possible_names in line_item_mapping.items():
            for idx in df.index:
                if isinstance(idx, str):
                    idx_lower = idx.lower().strip()
                    if any(name in idx_lower for name in possible_names):
                        extracted_items[standard_name] = df.loc[idx]
                        break
        
        return extracted_items
    
    def parse_balance_sheet(self, sheet_name: str = None) -> Dict[str, pd.Series]:
        """
        Parse balance sheet and extract key line items
        
        Returns:
            Dictionary with standard line items
        """
        if sheet_name is None:
            statements = self.find_financial_statement_sheets()
            sheet_name = statements.get('balance_sheet')
            
        if sheet_name is None:
            raise ValueError("Balance sheet sheet not found")
        
        df = self.extract_financial_statement(sheet_name)
        
        # Map common line item names
        line_item_mapping = {
            'cash': ['cash', 'cash and equivalents', 'cash & equivalents'],
            'accounts_receivable': ['accounts receivable', 'receivables', 'trade receivables'],
            'inventory': ['inventory', 'inventories'],
            'current_assets': ['current assets', 'total current assets'],
            'fixed_assets': ['fixed assets', 'pp&e', 'property plant equipment', 'ppe'],
            'total_assets': ['total assets', 'assets'],
            'accounts_payable': ['accounts payable', 'payables', 'trade payables'],
            'current_liabilities': ['current liabilities', 'total current liabilities'],
            'long_term_debt': ['long-term debt', 'long term debt', 'lt debt'],
            'total_liabilities': ['total liabilities', 'liabilities'],
            'shareholders_equity': ['shareholders equity', 'stockholders equity', 'equity', 'total equity'],
            'total_liabilities_equity': ['total liabilities and equity', 'total liab & equity']
        }
        
        extracted_items = {}
        
        for standard_name, possible_names in line_item_mapping.items():
            for idx in df.index:
                if isinstance(idx, str):
                    idx_lower = idx.lower().strip()
                    if any(name in idx_lower for name in possible_names):
                        extracted_items[standard_name] = df.loc[idx]
                        break
        
        return extracted_items
    
    def parse_cash_flow_statement(self, sheet_name: str = None) -> Dict[str, pd.Series]:
        """
        Parse cash flow statement and extract key line items
        
        Returns:
            Dictionary with standard line items
        """
        if sheet_name is None:
            statements = self.find_financial_statement_sheets()
            sheet_name = statements.get('cash_flow')
            
        if sheet_name is None:
            raise ValueError("Cash flow statement sheet not found")
        
        df = self.extract_financial_statement(sheet_name)
        
        # Map common line item names
        line_item_mapping = {
            'operating_cf': ['cash from operations', 'operating cash flow', 'cfo', 'cash from operating'],
            'capex': ['capital expenditures', 'capex', 'purchase of ppe', 'capital expenditure'],
            'investing_cf': ['cash from investing', 'investing cash flow', 'cfi'],
            'financing_cf': ['cash from financing', 'financing cash flow', 'cff'],
            'net_change_cash': ['net change in cash', 'net increase in cash', 'change in cash']
        }
        
        extracted_items = {}
        
        for standard_name, possible_names in line_item_mapping.items():
            for idx in df.index:
                if isinstance(idx, str):
                    idx_lower = idx.lower().strip()
                    if any(name in idx_lower for name in possible_names):
                        extracted_items[standard_name] = df.loc[idx]
                        break
        
        return extracted_items
    
    def extract_all_statements(self) -> Dict[str, Dict[str, pd.Series]]:
        """
        Extract all three financial statements
        
        Returns:
            Dictionary containing income statement, balance sheet, and cash flow data
        """
        financial_statements = {}
        
        try:
            financial_statements['income_statement'] = self.parse_income_statement()
        except Exception as e:
            print(f"Warning: Could not parse income statement: {str(e)}")
            financial_statements['income_statement'] = {}
        
        try:
            financial_statements['balance_sheet'] = self.parse_balance_sheet()
        except Exception as e:
            print(f"Warning: Could not parse balance sheet: {str(e)}")
            financial_statements['balance_sheet'] = {}
        
        try:
            financial_statements['cash_flow'] = self.parse_cash_flow_statement()
        except Exception as e:
            print(f"Warning: Could not parse cash flow statement: {str(e)}")
            financial_statements['cash_flow'] = {}
        
        return financial_statements
    
    def validate_data(self, data: Dict) -> Tuple[bool, List[str]]:
        """
        Validate extracted financial data
        
        Returns:
            Tuple of (is_valid, list_of_issues)
        """
        issues = []
        
        # Check for required line items
        required_items = {
            'income_statement': ['revenue', 'net_income'],
            'balance_sheet': ['total_assets', 'total_liabilities', 'shareholders_equity'],
            'cash_flow': ['operating_cf']
        }
        
        for statement, items in required_items.items():
            if statement in data:
                for item in items:
                    if item not in data[statement]:
                        issues.append(f"Missing required item: {statement}.{item}")
        
        # Balance sheet should balance
        if 'balance_sheet' in data:
            bs = data['balance_sheet']
            if all(item in bs for item in ['total_assets', 'total_liabilities', 'shareholders_equity']):
                assets = bs['total_assets']
                liab_equity = bs['total_liabilities'] + bs['shareholders_equity']
                
                # Check if they're close (within 1%)
                diff_pct = abs(assets - liab_equity) / assets if assets != 0 else 0
                if diff_pct > 0.01:
                    issues.append(f"Balance sheet doesn't balance: Assets vs Liab+Equity difference = {diff_pct*100:.1f}%")
        
        is_valid = len(issues) == 0
        return is_valid, issues
    
    def get_sheet_names(self) -> List[str]:
        """Get list of all sheet names in workbook"""
        return list(self.workbook_data.keys())
    
    def get_sheet_data(self, sheet_name: str) -> pd.DataFrame:
        """Get raw data from a specific sheet"""
        if sheet_name not in self.workbook_data:
            raise ValueError(f"Sheet '{sheet_name}' not found")
        return self.workbook_data[sheet_name]


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    # Example: Process an Excel file with financial statements
    
    # Create sample Excel file for demonstration
    print("Excel Processor - Example Usage")
    print("=" * 60)
    
    # If you have an actual Excel file:
    # processor = ExcelProcessor("path/to/your/financial_statements.xlsx")
    # statements = processor.extract_all_statements()
    # print(statements)
    
    print("\nThis script can process Excel files containing:")
    print("- Income Statement (P&L)")
    print("- Balance Sheet")
    print("- Cash Flow Statement")
    print("\nUsage:")
    print("  processor = ExcelProcessor('financial_statements.xlsx')")
    print("  statements = processor.extract_all_statements()")
    print("  print(statements)")

