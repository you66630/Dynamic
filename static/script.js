const DarkBtn = document.getElementById('DarkBtn');

function trueDarkMode(isDark) {
    if (isDark) {
        document.body.classList.add("darkmode");
        DarkBtn.innerHTML = "Light Mode";
    } else {
        document.body.classList.remove("darkmode");
        DarkBtn.innerHTML = "Dark Mode";

    }
}

const isDarkMode = localStorage.getItem("darkmode") === "true";
trueDarkMode(isDarkMode);

DarkBtn.addEventListener("click", () => {
    const isDark = !document.body.classList.contains("darkmode");
    trueDarkMode(isDark);
    localStorage.setItem('darkmode', isDark);
});
