const fs = require('fs');
const path = require('path');

const rootDir = __dirname;
const hubDir = path.join(rootDir, 'Apex Tax Practice Hub');
const distDir = path.join(rootDir, 'dist');

console.log('=== Building Mobile Web Distribution Bundle for Android APK ===');
console.log('Source Directory:', hubDir);
console.log('Target Directory:', distDir);

// 1. Ensure dist clean directory
if (fs.existsSync(distDir)) {
  fs.rmSync(distDir, { recursive: true, force: true });
}
fs.mkdirSync(distDir, { recursive: true });

// Helper to copy directory recursively
function copyDirSync(src, dest) {
  if (!fs.existsSync(src)) return;
  fs.mkdirSync(dest, { recursive: true });
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDirSync(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

// 2. Copy static asset directories: forms, sample_slips, js
console.log('Copying forms, sample_slips, and js libraries...');
copyDirSync(path.join(hubDir, 'forms'), path.join(distDir, 'forms'));
copyDirSync(path.join(hubDir, 'sample_slips'), path.join(distDir, 'sample_slips'));
copyDirSync(path.join(hubDir, 'js'), path.join(distDir, 'js'));

// 3. Copy main HTML pages
const htmlPages = ['returns.html', 'return_1040.html', 'curriculum.html', 'tasks.html'];
for (const page of htmlPages) {
  const src = path.join(hubDir, page);
  if (fs.existsSync(src)) {
    fs.copyFileSync(src, path.join(distDir, page));
    console.log(`✓ Copied ${page}`);
  }
}

// 4. Create index.html as the primary entry point for Android WebView (loads returns.html directly)
const returnsPath = path.join(hubDir, 'returns.html');
if (fs.existsSync(returnsPath)) {
  fs.copyFileSync(returnsPath, path.join(distDir, 'index.html'));
  console.log('✓ Created index.html (Default Android Launcher Entry point)');
}

console.log('=== Mobile Web Distribution Staged Successfully in dist/ ===');

