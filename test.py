#!/usr/bin/env python3
"""
Test Runner for Strobes GraphQL Client Examples
This script runs all example files in the examples directory to verify functionality.
"""

import os
import sys
import importlib.util
import time
from datetime import datetime

def load_module_from_file(file_path):
    """Load a Python module from file path"""
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def run_test(file_path):
    """Run a single test file and return status"""
    try:
        print(f"\n{'='*80}")
        print(f"Running: {os.path.basename(file_path)}")
        print(f"{'='*80}")
        
        module = load_module_from_file(file_path)
        
        # Most example files have a main() function
        if hasattr(module, 'main'):
            module.main()
        # Some might have specific test functions
        elif hasattr(module, 'create_sample_engagement'):
            module.create_sample_engagement()
        elif hasattr(module, 'fetch_all_vault_attachments'):
            module.fetch_all_vault_attachments()
        
        return True
    except Exception as e:
        print(f"❌ Error in {os.path.basename(file_path)}: {str(e)}")
        return False

def main():
    # Get the examples directory path
    examples_dir = os.path.join(os.path.dirname(__file__), 'examples')
    
    # List of files to skip
    skip_files = {'__init__.py', '__pycache__', 'example.py'}  # Added example.py to skip list
    
    # Get all Python files in examples directory
    test_files = [
        os.path.join(examples_dir, f) 
        for f in os.listdir(examples_dir) 
        if f.endswith('.py') and f not in skip_files
    ]
    
    # Sort files to ensure consistent order
    test_files.sort()
    
    print(f"\n🚀 Starting Strobes GraphQL Client Tests")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Found {len(test_files)} test files")
    print("Skipping: example.py (reference file)")
    print()
    
    # Track results
    results = {
        'passed': [],
        'failed': []
    }
    
    # Run each test file
    for file_path in test_files:
        file_name = os.path.basename(file_path)
        start_time = time.time()
        
        success = run_test(file_path)
        duration = time.time() - start_time
        
        if success:
            results['passed'].append((file_name, duration))
        else:
            results['failed'].append((file_name, duration))
    
    # Print summary
    print(f"\n{'='*80}")
    print("Test Summary")
    print(f"{'='*80}")
    print(f"Total Tests: {len(test_files)}")
    print(f"Passed: {len(results['passed'])}")
    print(f"Failed: {len(results['failed'])}")
    
    if results['passed']:
        print("\n✅ Passed Tests:")
        for name, duration in results['passed']:
            print(f"  - {name} ({duration:.2f}s)")
    
    if results['failed']:
        print("\n❌ Failed Tests:")
        for name, duration in results['failed']:
            print(f"  - {name} ({duration:.2f}s)")
    
    # Exit with status code
    sys.exit(len(results['failed']))

if __name__ == "__main__":
    main() 