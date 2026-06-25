console.log("Contact Manager Loaded");

const themeToggle =
    document.getElementById("theme-toggle");

const themeIcon =
    document.getElementById("theme-icon");

const savedTheme =
    localStorage.getItem("theme");

if (savedTheme === "dark") {

    document.body.classList.add("dark-mode");

    themeIcon.className =
        "bi bi-moon-stars-fill";
}

themeToggle.addEventListener(
    "click",
    () => {

        document.body.classList.toggle(
            "dark-mode"
        );

        if (
            document.body.classList.contains(
                "dark-mode"
            )
        ) {

            localStorage.setItem(
                "theme",
                "dark"
            );

            themeIcon.className =
                "bi bi-moon-stars-fill";

        } else {

            localStorage.setItem(
                "theme",
                "light"
            );

            themeIcon.className =
                "bi bi-sun";

        }

    }
);