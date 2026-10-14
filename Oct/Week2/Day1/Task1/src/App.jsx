import React from 'react'
import Card from './Card'

function App() {


   let animals = [
    {
      img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4P8qUnTDtYQMSIdxAacWAaKzrWKDmYRKI4KnfxpNkr3QvEnqZsnHcKHWQ&s=10",
      title: "Bear",
      desc: "this is a Bear",
    },
    {
      img: "https://t3.ftcdn.net/jpg/05/09/93/68/360_F_509936859_0qAdnRP3jI0awRaQX1txwyE31gYjer7k.jpg",
      title: "Fox",
      desc: "this is wild Animal",
    },
    {
      img: "https://res.cloudinary.com/roundglass/image/upload/f_auto/v1626693793/roundglass/ranthambore-lightning-young-adult-walking-aditya-dicky-singh-scaled_jsocc2.jpg",
      title: "Tiger",
      desc: "this is bengol tiger",
    },
    {
      img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6BBavybTn_v_zadRTEbcrkmZB5FIGcPwGsXUYXFIZwg&s",
      title: "Mouse",
      desc: "This is a mouse",
    },
    {
      img: "https://i.pinimg.com/736x/1f/48/ec/1f48ecc2a11c71aaf936a9b071072bb5.jpg",
      title: "Rabbit",
      desc: "This is a cute Rabbit",
    },
    {
      img: "https://images.pexels.com/photos/47547/squirrel-animal-cute-rodents-47547.jpeg?cs=srgb&dl=pexels-pixabay-47547.jpg&fm=jpg",
      title: "Squirrel",
      desc: "This is a Squirrel",
    },
    {
      img: "https://www.shropshirewildlifetrust.org.uk/sites/default/files/styles/spotlight_default/public/2017-12/Fallow%20Deer%20-%20July%202015%20Gillian%20Day%202.JPG?h=e7eded5b&itok=8a3OHkHa",
      title: "Deer",
      desc: "This is a Deer",
    },
    {
      img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp9AY4y-v0v7LpcfeWcYmL0CXzkvCYqcY3y6BNBDycmw&s",
      title: "Dog",
      desc: "This is a Dog",
    },
  ];


  return (
    <div >
      <h1 className='bg-green-500 text-center font-bold'>Welcome to my Animal Card</h1>

      <div className="grid grid-cols-4 gap-4">
        {animals?.map((animal) => (
          <Card animal={animal} />
        ))}
      </div>
    </div>
  )
}

export default App