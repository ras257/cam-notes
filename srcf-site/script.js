function detectTheme() {
  const stored = localStorage.getItem("darkTheme");
  if (stored !== null) return stored === "true";

  if (!window.matchMedia) return true;
  return window.matchMedia('(prefers-color-scheme: dark)').matches;
}

function toggleTheme() {
  darkMode = !darkMode;
  localStorage.setItem("darkTheme", darkMode);
  updateTheme();
}

function updateTheme() {
  if (darkMode) {
    root.classList.remove('light');
    root.classList.add('dark');
  } else {
    root.classList.remove('dark');
    root.classList.add('light');
  };
}

const root = document.documentElement;
let darkMode = detectTheme();
updateTheme();

